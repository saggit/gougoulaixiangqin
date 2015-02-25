#coding: utf-8
from django.shortcuts import render
from uauth.utils import auth_required
from django.views.decorators.csrf import csrf_exempt
from gougoulaixiangqin import utils
from gougou.models import GouGou, GouGouForm

@csrf_exempt
@utils.json_response_result
@auth_required
def gougou_edit(request, user):
    gougou_id = int(request.POST.get("gougou_id", 0))
    if gougou_id != 0:
        gougou = GouGou.objects.get(pk=gougou_id)
        gougou_f = GouGouForm(request.POST, instance=gougou)
        gougou_f.save()
    else:
        gougou_f = GouGouForm(request.POST)
        gougou = gougou_f.save(commit=False)
        gougou.master = user
        gougou.geo_hash = user.geo_hash
        gougou.latest_longitude = user.latest_longitude
        gougou.latest_latitude = user.latest_latitude
        gougou.updated_coordinate_time = user.updated_coordinate_time
        gougou.save()
    return {"code": 0, "data": {"message": u"更新成功"}}

@csrf_exempt
@utils.json_response_result
@auth_required
def get_my_gougous(request, user):
    my_gougous = GouGou.objects.filter(master=user).\
                 order_by("-created_at").values('nick_name', 'photo', 'age', 'gender', 'requirement', 'description')
    return {"code": 0, "data": {"gougous": list(my_gougous)}}
