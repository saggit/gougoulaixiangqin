# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gougou', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gougou',
            name='genre_name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u72d7\u72d7\u54c1\u79cd', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gougou',
            name='opp',
            field=models.IntegerField(default=0, verbose_name='\u64cd\u4f5c\u7c7b\u578b'),
            preserve_default=True,
        ),
    ]
