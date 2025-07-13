from django.urls import path
from .views import ChatMessageListCreateView

urlpatterns = [
    path('api/chat', ChatMessageListCreateView.as_view(), name='chat-list-create'),
]
