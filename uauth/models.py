#coding: utf-8

from django.db import models
from django.db.models.signals import pre_save
import uuid, hashlib

class User(models.Model):
    USER_TYPE_CHOICES = ((0, u"微博"), (1, u"腾讯"), (2, u"手机"))
    nick_name = models.CharField(u"昵称", max_length=200, null=True, blank=True)
    chat_account = models.CharField(u"聊天账户名称", max_length=300, null=True, blank=True)
    chat_account_pd = models.CharField(u"聊天账户密码", max_length=300, null=True, blank=True)
    user_type = models.IntegerField(u"用户类型", choices=USER_TYPE_CHOICES, max_length=50, default=-1)
    user_photo = models.CharField(u"用户头像", max_length=300, null=True, blank=True)
    user_access_token = models.CharField(u"系统accesstoken", max_length=200, null=True, blank=True)
    latest_longitude = models.FloatField(u"经度", null=True, blank=True)
    latest_latitude = models.FloatField(u"纬度", null=True, blank=True)
    geo_hash = models.CharField(u"geo hash", max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True, null=True)
    updated_coordinate_time = models.DateTimeField(u"地址更新时间", null=True, blank=True)

    @staticmethod
    def generate_user_access_token(): return str(uuid.uuid1())

class WeiboUser(User):
    user_id = models.CharField(u"微博用户id", max_length=30)
    access_token = models.CharField(u"微博授权token", max_length=200)
    expiration_date = models.DateTimeField(u"授权Token过期时间", null=True, blank=True)

class PhoneUser(User):
    user_phone = models.CharField(u"用户电话", max_length=30)
    hashed_password = models.CharField(u"加密密码", max_length=200, null=True, blank=True)

    def set_nick_name(self):
        self.nick_name = "abcd"

    def set_hashed_password(self, plain_password):
        hashed_password = PhoneUser.hash_password(plain_password)
        self.hashed_password = hashed_password

    @staticmethod
    def hash_password(plain_password):
        sha1 = hashlib.sha1()
        sha1.update(plain_password)
        return sha1.hexdigest()

class PhoneCode(models.Model):
    phone = models.CharField(u"用户电话", max_length=30)
    code = models.CharField(u"验证码", max_length=10)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

class TencentUser(User):
    pass

class UserOldCoordinate(models.Model):
    longitude = models.FloatField(u"经度")
    latitude = models.FloatField(u"纬度")
    user = models.ForeignKey('User')
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True)

def save_with_user_access_token(sender, **kwargs):
    instance = kwargs["instance"]
    if not instance.user_access_token:
        instance.user_access_token = User.generate_user_access_token()

pre_save.connect(save_with_user_access_token, sender=WeiboUser)
pre_save.connect(save_with_user_access_token, sender=PhoneUser)
