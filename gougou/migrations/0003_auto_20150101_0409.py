# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gougou', '0002_auto_20150101_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='gougou',
            name='latest_latitude',
            field=models.FloatField(null=True, verbose_name='\u7eac\u5ea6', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gougou',
            name='latest_longitude',
            field=models.FloatField(null=True, verbose_name='\u7ecf\u5ea6', blank=True),
            preserve_default=True,
        ),
    ]
