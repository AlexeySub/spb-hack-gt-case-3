from channels.generic.websocket import SyncConsumer, WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class Consumer(SyncConsumer):
    def connect(self):
        self.room_group_name = 'stream'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print("print text_data!!!:", text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'stream_message',
                'message': message,
            }
        )

        self.send(text_data=json.dumps({
            'message': message
        }))

    def stream_message(self, event):
        message = event['message']

        # Send message to websocket
        self.send(text_data=json.dumps({'message': message}))