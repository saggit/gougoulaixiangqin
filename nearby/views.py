from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from uauth.utils import auth_required
from gougoulaixiangqin.utils import json_response_result
import json, requests, geohash
from nearby.service import *
from django.conf import settings
from gougou.models import *
from django.db.models import Q
from nearby.utils import distance

@csrf_exempt
@json_response_result
@auth_required
def get_nearby_dogs(request, user):
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    gender = request.POST.get("gender", None)
    genre_name = request.POST.get("gener_name", None)
    opp = request.POST.get("opp", None)
    page = request.POST.get("page", 1)
    geo_hash = update_user_coordinate(longitude, latitude, user)
    part_geo_hash = geo_hash[:settings.GEO_HASH_NUM]
    query_total = Q(geo_hash__startswith=part_geo_hash)
    if gender: query_total &= Q(gender=gender)
    if genre_name: query_total &= Q(genre_name=genre_name)
    if opp: query_total &= Q(opp=opp)
    gougous = GouGou.objects.filter(query_total)[:1200].\
              values('nick_name', 'photo', 'age', 'gender',
                     'requirement', 'description', 'latest_longitude', 'latest_latitude')
    results = []
    for gougou in gougous:
        gougou["distance"] = distance([gougou["latest_latitude"], gougou["latest_longitude"]],
                                      [float(latitude), float(longitude)])
        results.append(gougou)
    results = sorted(results, key=lambda x: x.get("distance", 1000))
    return {"code": 0, "data": {"gougous": list(results)}}
