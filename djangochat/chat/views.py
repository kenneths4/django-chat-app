from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
# Create your views here.
from .models import Chat, Message

@login_required
@csrf_protect
def chats(request):
    chats = Chat.objects.all

    return render(request, "chat/chats.html", {"chats" : chats})
        




@login_required
@csrf_protect
def chat(request, slug):
    chat = Chat.objects.get(slug=slug)

    messages = Message.objects.filter(chat=chat)[0:25]
    return render(request, "chat/chat.html", {'chat' : chat, 'messages': messages})