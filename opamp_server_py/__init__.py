from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from contextlib import asynccontextmanager
from fastapi.logger import logger
import json

from opamp_server_py.utils.clients import mongo_client, mongo_agents_collection
from opamp_server_py.utils.proto import (
    load_pb2_modules , 
    decode_opamp_message,
    sym_db
)

from opamp_server_py.types.opamp_p2p import AgentToServer


@asynccontextmanager
async def lifespan(app : FastAPI):
    """Load protobuf modules on startup"""
    # Replace with your actual module names
    load_pb2_modules([
        "opamp_server_py.types.anyvalue_pb2",  # Update with your actual module names
        "opamp_server_py.types.opamp_pb2"  # Update with your actual module names
    ])
    yield
    mongo_client.close()


app = FastAPI(lifespan=lifespan)

@app.get('/types')
async def get_types():
    return [cls.DESCRIPTOR.full_name for cls in sym_db._classes.values()] # type: ignore

@app.get('/health')
async def health():
    return "ok"

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive binary data
            data = await websocket.receive_bytes()
            
            # Decode the OpAMP message
            header, message_dict, message_type = decode_opamp_message(data)
            
            if message_dict is not None:
                if message_type:
                    print(f"Received OpAMP message of type: {message_type}")
                else:
                    print("Received empty OpAMP message (valid)")
                if message_type == 'opamp.proto.AgentToServer':
                    data = AgentToServer.model_validate(message_dict)
                    mongo_agents_collection.update_one({"instance_uid" : data.instance_uid},{"$set": data.model_dump(exclude_none=True,exclude_unset=True)}, upsert=True)
            else:
                print(f"Failed to decode OpAMP message with header: {header}")
    
    except WebSocketDisconnect:
        logger.info("Client disconnected")