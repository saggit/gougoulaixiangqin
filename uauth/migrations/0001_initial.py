# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(max_length=200, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('user_type', models.CharField(default=-1, max_length=50, verbose_name='\u7528\u6237\u7c7b\u578b', choices=[(0, '\u5fae\u535a'), (1, '\u817e\u8baf')])),
                ('user_photo', models.CharField(max_length=300, null=True, verbose_name='\u7528\u6237\u5934\u50cf', blank=True)),
                ('user_access_token', models.CharField(max_length=200, null=True, verbose_name='\u7cfb\u7edfaccesstoken', blank=True)),
                ('latest_longitude', models.FloatField(null=True, verbose_name='\u7ecf\u5ea6', blank=True)),
                ('latest_latitude', models.FloatField(null=True, verbose_name='\u7eac\u5ea6', blank=True)),
                ('geo_hash', models.CharField(max_length=50, null=True, verbose_name='geo hash', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_coordinate_time', models.DateTimeField(null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserOldCoordinate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.FloatField(verbose_name='\u7ecf\u5ea6')),
                ('latitude', models.FloatField(verbose_name='\u7eac\u5ea6')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeiboUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='uauth.User')),
                ('user_id', models.CharField(max_length=30, verbose_name='\u5fae\u535a\u7528\u6237id')),
                ('access_token', models.CharField(max_length=200, verbose_name='\u5fae\u535a\u6388\u6743token')),
                ('expiration_date', models.DateTimeField(null=True, verbose_name='\u6388\u6743Token\u8fc7\u671f\u65f6\u95f4', blank=True)),
            ],
            options={
            },
            bases=('uauth.user',),
        ),
        migrations.AddField(
            model_name='useroldcoordinate',
            name='user',
            field=models.ForeignKey(to='uauth.User'),
            preserve_default=True,
        ),
    ]
