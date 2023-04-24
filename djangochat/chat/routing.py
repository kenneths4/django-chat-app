from django.urls import path

from . import consumers

websocket_url_patterns = [
    path('ws/<str:chat_name>', consumers.ChatConsumer.as_asgi()),
]