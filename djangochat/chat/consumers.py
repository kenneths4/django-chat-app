import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_name = self.scope["url_route"]["kwargs"]["chat_name"]
        self.chat_group_name = "%s_group" % self.chat_name 

        # add group to channel layers
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        # connect to channel
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )