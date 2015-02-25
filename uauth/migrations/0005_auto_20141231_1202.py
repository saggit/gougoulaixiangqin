# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0004_auto_20141231_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phoneuser',
            name='password_token',
        ),
        migrations.AddField(
            model_name='phoneuser',
            name='hashed_password',
            field=models.CharField(max_length=200, null=True, verbose_name='\u52a0\u5bc6\u5bc6\u7801', blank=True),
            preserve_default=True,
        ),
    ]
