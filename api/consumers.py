from channels.consumer import SyncConsumer
import json


class Consumer(SyncConsumer):
    def websocket_connect(self, event):
        print("SOCKET CONNECT")
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print("message", event)
        self.send({
            'type': 'websocket.send',
            'text': event['text'],
        })
