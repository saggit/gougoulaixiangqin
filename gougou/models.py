#coding: utf-8
from django.db import models
from uauth.models import User
from django.forms import ModelForm

class GouGouGenre(models.Model):
    genre_name = models.CharField(u"品种名称", max_length=100)

class GouGou(models.Model):
    GENDER_CHOICES = ((0, u"帅哥"), (1, u"美女"))
    OPP_CHOICES = ((0, u"相亲"), (2, u"出售"), (3, u"寄养"))
    genre_name = models.CharField(u"狗狗品种", max_length=100, null=True, blank=True)
    nick_name = models.CharField(u"狗狗姓名", max_length=100)
    photo = models.CharField(u"狗狗头像", max_length=500, null=True, blank=True)
    age = models.IntegerField(u"狗狗年龄", default=1)
    description = models.CharField(u"狗狗介绍", max_length=2000, default='')
    gender = models.IntegerField(u"狗狗性别", choices=GENDER_CHOICES, default=0)
    latest_longitude = models.FloatField(u"经度", null=True, blank=True)
    latest_latitude = models.FloatField(u"纬度", null=True, blank=True)
    geo_hash = models.CharField(u"geo hash", max_length=50, null=True, blank=True)
    updated_coordinate_time = models.DateTimeField(u"地址更新时间", null=True)
    requirement = models.CharField(u"主人要求", max_length=2000, default='')
    opp = models.IntegerField(u"操作类型", default=0)
    created_at = models.DateTimeField(u"创建时间", auto_now_add=True, null=True)
    master = models.ForeignKey(User)

class GouGouPhotos(models.Model):
    photo_url = models.CharField(u"图片地址", max_length=500)
    order = models.IntegerField(u"照片顺序", default=0)
    gougou = models.ForeignKey(GouGou)

class GouGouForm(ModelForm):
    class Meta:
        model = GouGou
        fields = ['nick_name', 'photo', 'age', 'gender', 'requirement', 'description']
