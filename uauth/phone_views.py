#coding: utf-8
from django.shortcuts import render
from uauth.models import User, PhoneUser
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from uauth.utils import auth_required
from uauth.models import PhoneCode
from gougoulaixiangqin.utils import json_response_result
from django.db.models import Q
import json, requests, geohash
import t189

@csrf_exempt
@json_response_result
def get_phone_vcode(request):
    phone = request.POST.get("phone")
    send = True
    try:
        exists_phonecodes = PhoneCode.objects.filter(phone=phone).order_by("-created_at")
        if exists_phonecodes:
            exists_phonecode = exists_phonecodes[0]
            now = datetime.now()
            delta = (now - exists_phonecode).total_seconds()
            if delta < 60: send = False
        if send:
            success, randcode = t189.send_message_code(phone)
        else:
            return {"code": 1002, "data": {"message": u"麻烦一分钟后再过来试吧~"}}
        if success:
            PhoneCode.objects.create(phone=phone, code=randcode)
            return {"code": 0, "data": {"message": u"验证码发送成功哦，记得检查短信哦^_^"}}
        else:
            return {"code": 1000, "data": {"message": u"亲，你是不是输错什么了啊？"}}
    except Exception, e:
        print e.message
        return {"code": 1001, "data": {"message": u"服务器开小差中，请稍后再试哦，^_^"}}

@csrf_exempt
@json_response_result
def phone_register(request):
    user_phone = request.POST.get("phone")
    password = request.POST.get("password")
    vcode = request.POST.get("vcode")
    exists_phone_user = PhoneUser.objects.filter(user_phone=user_phone)
    if exists_phone_user: return {"code": -1, "data": {"message": u"亲，该手机已经注册成功哦~"}}
    exists_phonecodes = PhoneCode.objects.filter(Q(phone=phone) & Q())

    phone_user = PhoneUser(user_phone=user_phone)
    phone_user.set_hashed_password(password)
    phone_user.user_type = 2
    phone_user.set_nick_name()
    phone_user.save()
    return {
        "code": 0, "data": {
            "id": phone_user.user_ptr_id, "user_access_token": phone_user.user_access_token,
            "name": phone_user.nick_name, "photo": phone_user.user_photo
        }
    }

@csrf_exempt
@json_response_result
def phone_login(request):
    user_phone = request.POST.get("phone")
    password = request.POST.get("password")
    hashed_password = PhoneUser.hash_password(password)
    exist_phone_users = PhoneUser.objects.filter(user_phone=user_phone, hashed_password=hashed_password)
    if exist_phone_users:
        phone_user = exist_phone_users[0]
        return {
            "code": 0, "data": {
                "id": phone_user.user_ptr_id, "user_access_token": phone_user.user_access_token,
                "name": phone_user.nick_name, "photo": phone_user.user_photo
            }
        }
    return {"code": -1, "data": {"message": u"手机或者密码不正确"}}

def forget_passwd(request):
    pass
