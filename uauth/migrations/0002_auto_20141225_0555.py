# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='updated_coordinate_time',
            field=models.DateTimeField(null=True, verbose_name='\u5730\u5740\u66f4\u65b0\u65f6\u95f4'),
            preserve_default=True,
        ),
    ]
