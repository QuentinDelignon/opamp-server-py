from fastapi import FastAPI , WebSocket , WebSocketDisconnect

app = FastAPI()

@app.get('/health')
async def health():
    return "ok"

@app.websocket('/ws')
async def websocket_endpoint(websocket : WebSocket):
    try:
        while True:
            data = await websocket.receive_json()
            await websocket.send_json(data)
    except WebSocketDisconnect:
        print("Client Disconnected")