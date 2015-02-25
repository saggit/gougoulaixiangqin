# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0003_phoneuser_tencentuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='updated_coordinate_time',
            field=models.DateTimeField(null=True, verbose_name='\u5730\u5740\u66f4\u65b0\u65f6\u95f4', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(default=-1, max_length=50, verbose_name='\u7528\u6237\u7c7b\u578b', choices=[(0, '\u5fae\u535a'), (1, '\u817e\u8baf'), (2, '\u624b\u673a')]),
            preserve_default=True,
        ),
    ]
