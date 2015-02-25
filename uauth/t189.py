import json
import hmac
import hashlib
import base64
import urllib, urllib2
import requests
import random
from time import strftime, localtime

APP_ID = "221055120000039260"
APP_SECRET = "7cb286b5371b7dad5c827e4a97c712a0"
from datetime import datetime
from collections import defaultdict, OrderedDict

def generate_url(data):
    keys = data.keys()
    keys.sort()
    data_o_url_part = '&'.join([key + "=" + data[key] for key in keys])
    hashed = hmac.new(APP_SECRET, data_o_url_part, hashlib.sha1).digest()
    return "%s&sign=%s" % (data_o_url_part, urllib.quote(hashed.encode("base64").strip()))

def get_timestamp():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

def get_access_token():
    code_url = "https://oauth.api.189.cn/emp/oauth2/v3/access_token"
    data = {
        "grant_type": "client_credentials",
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    }
    result = requests.post(code_url, data=data).json()
    return result["access_token"]


def get_randcode_token():
    access_token = get_access_token()
    token_url = "http://api.189.cn/v2/dm/randcode/token"
    data = {
        "app_id": APP_ID,
        "access_token": str(access_token),
        "timestamp": str(get_timestamp())
    }
    url = generate_url(data)
    print data
    result = requests.get(token_url+"?"+url).json()
    return result["token"]

def get_rand_code():
    return "".join([str(random.randint(0,9)) for i in range(6)])

def send_message_code(phone):
    send_url = "http://api.189.cn/v2/dm/randcode/sendSms"
    access_token = get_access_token()
    token = get_randcode_token()
    randcode = get_rand_code()
    data = {
        'app_id': APP_ID,
        'access_token': str(access_token),
        'timestamp': str(get_timestamp()),
        'token': token, 'phone': phone,
        'exp_time':'30', 'randcode': randcode
    }
    data = generate_url(data)
    req = urllib2.Request(send_url, data)
    result = json.loads(urllib2.urlopen(req).read())
    print result
    return result.get("res_code", -1) == 0, randcode

if __name__ == "__main__":
    print send_message_code("15601672922")
