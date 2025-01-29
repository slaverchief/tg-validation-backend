from .views import *
from django.urls import path

urlpatterns = [
    path('check', check_user),
    path('get/<int:group_id>', get_chats),
    path('get', get_groups)
]
