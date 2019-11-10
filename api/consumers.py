from channels.generic.websocket import AsyncWebsocketConsumer
import json


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def websocket_receive(self, message):
        print("message", message)
        data = json.load(message["text"])
        print("message text:", data)
        await self.send({
            'message': data
        })
