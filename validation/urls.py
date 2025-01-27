from .views import *
from django.urls import path

urlpatterns = [
    path('check', check_user),
    path('get', get_groups)
]
