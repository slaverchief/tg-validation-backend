import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import TGuser

def check_user(request):
    user = json.loads(request.body.decode('utf-8')).get('user')
    try:
        TGuser.objects.get(tgid=user)
        return HttpResponse(status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
