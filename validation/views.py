import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from .models import *

def check_user(request):
    user = json.loads(request.body.decode('utf-8')).get('user')
    try:
        TGuser.objects.get(tgid=user)
        return HttpResponse(status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

def get_chats(request, group_id):
    group = Group.objects.get(pk=group_id)
    return JsonResponse([(chat.chatid, chat.topic_id) for chat in group.chats.all()], safe=False)

def get_groups(request):
    return JsonResponse([(group.pk, group.name) for group in Group.objects.all()], safe=False)