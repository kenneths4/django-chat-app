from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Chat

@login_required
def chats(request):
    chats = Chat.objects.all

    return render(request, "chats.html", {"chats" : chats})
