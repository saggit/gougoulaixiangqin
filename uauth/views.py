#coding: utf-8
from django.shortcuts import render
from uauth.models import WeiboUser, User, UserOldCoordinate, PhoneUser
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from uauth.utils import auth_required
from gougoulaixiangqin.utils import json_response_result
import json, requests, geohash

@csrf_exempt
@json_response_result
def weibo_login(request):
    if request.method != "POST":
        return HttpResponse(json.dumps({"code": -2, "data": {"message": "method does not support"}}))
    try:
        user_id = request.POST.get("userId")
        access_token = request.POST.get("accessToken")
        expiration_date = request.POST.get("expirationDate")
        expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
    except Exception, e:
        return HttpResponse(json.dumps({"code": -1, "data": {"message": u"错误的参数"}}))
    data = {"access_token": access_token, "uid": user_id}
    try:
        data_info = requests.get("https://api.weibo.com/2/users/show.json", params=data).json()
        if str(data_info.get("id")) != str(user_id): raise Exception(u"错误的参数")
    except Exception, e:
        return HttpResponse(json.dumps({"code": 1001, "data": {"message": u"微博暂时无法访问，请稍后重试"}}))
    weibo_users = WeiboUser.objects.filter(user_id=user_id)
    if not weibo_users:
        weibo_user = WeiboUser(
            user_id=user_id, access_token=access_token,
            expiration_date=expiration_date, user_type = 0,
            nick_name = data_info.get("screen_name", ""),
            user_photo = data_info.get("profile_image_url", "")
        )
    else:
        weibo_user = weibo_users[0]
        weibo_user.access_token = access_token
    weibo_user.save()
    return {
        "code": 0, "data": {
            "id": weibo_user.user_ptr_id, "user_access_token": weibo_user.user_access_token,
            "name": weibo_user.nick_name, "photo": weibo_user.user_photo
        }}
