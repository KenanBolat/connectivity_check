import websockets
import asyncio


async def listen():
    # url = "ws://<location>"
    url = "ws://simple-websocket-server-echo.glitch.me/"
    url = "ws://127.0.0.1:7890/"
    async with websockets.connect(url) as websocket:
        await websocket.send("Hello Server!")
        msg = await websocket.recv()
        print(msg)

asyncio.get_event_loop().run_until_complete(listen())
