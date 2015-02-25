# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0005_auto_20141231_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=30, verbose_name='\u7528\u6237\u7535\u8bdd')),
                ('code', models.CharField(max_length=10, verbose_name='\u9a8c\u8bc1\u7801')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
