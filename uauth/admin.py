from django.contrib import admin

from uauth.models import *

admin.site.register(WeiboUser)
admin.site.register(PhoneUser)

admin.site.register(UserOldCoordinate)
