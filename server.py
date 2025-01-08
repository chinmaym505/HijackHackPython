import asyncio
import websockets

async def server_handler(websocket, path):
    client_ip = websocket.remote_address[0]
    print(f"Client connected from IP: {client_ip}")
    try:
        while True:
            # Read command from server console
            command = input("Enter command: ")
            await websocket.send(command)
            if command == "exit":
                print("Closing connection")
                await websocket.close()
                break
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def main():
    server = await websockets.serve(server_handler, "localhost", 8765)
    print("Server started at ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
