#coding: utf-8
from django.http import HttpResponse
from uauth.models import WeiboUser, User
from datetime import datetime
from collections import defaultdict, OrderedDict
import json
import hmac
import hashlib
import base64
import urllib

def auth_required(func):
    def wraps(request, *args, **kwargs):
        uid = request.GET.get("uid", 0)
        uact = request.GET.get("uact", "")
        try:
            us = User.objects.get(pk=int(uid), user_access_token=uact)
        except:
            return {"code": -1000, "data": {"message": u"接口未授权"}}
        return func(request, us, *args, **kwargs)
    return wraps
