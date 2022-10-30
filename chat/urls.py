from django.urls import path
from . import views

urlpatterns = [
    path('suggested_chats/', views.get_suggested_chats)
]
