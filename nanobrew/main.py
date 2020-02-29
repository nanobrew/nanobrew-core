import asyncio
from .presentation.http.server import Server
from .foo import read_sensors

def main():
    read_sensors()
    print("is this executed?")

    httpServer = Server()
    httpServer.run()
