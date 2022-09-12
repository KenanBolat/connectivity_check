import websockets
import asyncio

PORT = 7890
print(f"Server listening on Port {PORT}")

connected = set()


async def echo(websocket, path):
    print("A client just connected")
    # Store a copy of the connected client
    connected.add(websocket)
    # Handle incoming messages
    try:
        async for message in websocket:
            print(f"Recived message from client:{message}")
        for conn in connected:
            if conn != websocket:
                await conn.send(f"Someone said: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(e)

start_server = websockets.serve(echo, 'localhost', PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()