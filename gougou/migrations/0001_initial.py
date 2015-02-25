# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0002_auto_20141225_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='GouGou',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(max_length=100, verbose_name='\u72d7\u72d7\u59d3\u540d')),
                ('photo', models.CharField(max_length=500, null=True, verbose_name='\u72d7\u72d7\u5934\u50cf', blank=True)),
                ('age', models.IntegerField(default=1, verbose_name='\u72d7\u72d7\u5e74\u9f84')),
                ('description', models.CharField(default=b'', max_length=2000, verbose_name='\u72d7\u72d7\u4ecb\u7ecd')),
                ('gender', models.IntegerField(default=0, verbose_name='\u72d7\u72d7\u6027\u522b', choices=[(0, '\u5e05\u54e5'), (1, '\u7f8e\u5973')])),
                ('requirement', models.CharField(default=b'', max_length=2000, verbose_name='\u4e3b\u4eba\u8981\u6c42')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('geo_hash', models.CharField(max_length=50, null=True, verbose_name='geo hash', blank=True)),
                ('updated_coordinate_time', models.DateTimeField(null=True, verbose_name='\u5730\u5740\u66f4\u65b0\u65f6\u95f4')),
                ('master', models.ForeignKey(to='uauth.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GouGouGenre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=100, verbose_name='\u54c1\u79cd\u540d\u79f0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GouGouPhotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo_url', models.CharField(max_length=500, verbose_name='\u56fe\u7247\u5730\u5740')),
                ('order', models.IntegerField(default=0, verbose_name='\u7167\u7247\u987a\u5e8f')),
                ('gougou', models.ForeignKey(to='gougou.GouGou')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
