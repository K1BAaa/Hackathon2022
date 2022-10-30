from django.shortcuts import render
from chat.models import SuggestedChats


def get_suggested_chats(request):
    chats_obj = SuggestedChats()
    chats_obj.define_chats()
    chats = {
        "recommended": chats_obj.user_chats,
        "negative": chats_obj.user_negative_chat
    }
    return render(request, chats)
