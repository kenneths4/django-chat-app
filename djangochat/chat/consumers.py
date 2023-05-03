import json

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name 

        # add group to channel layers
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # connect to channel
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        print(data)
        chat = data["chat"]

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message":message,
                "username":username,
                "chat":chat
            }
        )
    
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        chat = event["chat"]

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "chat": chat,
        }))
