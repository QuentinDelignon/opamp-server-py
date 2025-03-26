from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, WebSocket, WebSocketDisconnect , HTTPException
from fastapi.logger import logger
from bson.json_util import _json_convert
import json

from opamp_server_py.utils.clients import mongo_client, mongo_agents_collection
from opamp_server_py.utils.proto import split_message
from opamp_server_py.types.opamp import AgentToServer


app = FastAPI()

@app.get('/types')
async def get_types():
    return [cls.DESCRIPTOR.full_name for cls in sym_db._classes.values()] # type: ignore

@app.get('/agents')
async def get_agents(page : int = 1) -> list[AgentToServer]:
    res = mongo_agents_collection.find({},limit=100,skip=(page-1)*100)
    res = [AgentToServer().from_dict(_json_convert(a))  for a in res]
    return res

@app.get('/agents/{agent_id}')
async def get_agent(agent_id : str) -> AgentToServer:
    res = mongo_agents_collection.find_one({'instance_uid': agent_id})
    if res is None:
        raise HTTPException(status_code=404,detail=f'Could not find agent with uid {agent_id}')
    return AgentToServer().from_dict(_json_convert(res))

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

            try:
                # split the header
                header, message_bytes = split_message(data)
                if message_bytes is not None:
                    data = AgentToServer().parse(message_bytes)
                    print("Receive AgentToServer Message")
                    mongo_agents_collection.update_one(
                        {"instance_uid" : data.instance_uid},
                        {"$set": data.to_dict()},
                        upsert=True
                    )
            except:
                print("Could not decode message")
    
    except WebSocketDisconnect:
        logger.info("Client disconnected")