# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0002_auto_20141225_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='uauth.User')),
                ('user_phone', models.CharField(max_length=30, verbose_name='\u7528\u6237\u7535\u8bdd')),
                ('password_token', models.CharField(max_length=200, verbose_name='\u5bc6\u7801token')),
            ],
            options={
            },
            bases=('uauth.user',),
        ),
        migrations.CreateModel(
            name='TencentUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='uauth.User')),
            ],
            options={
            },
            bases=('uauth.user',),
        ),
    ]
