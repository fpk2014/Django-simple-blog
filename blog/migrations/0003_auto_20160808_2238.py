# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160808_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
        migrations.RemoveField(
            model_name='article',
            name='topped',
        ),
        migrations.RemoveField(
            model_name='article',
            name='views',
        ),
    ]
