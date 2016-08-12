# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160808_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(help_text=b'\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x8c\xe5\xa6\x82\xe8\x8b\xa5\xe4\xb8\xba\xe7\xa9\xba\xe5\xb0\x86\xe6\x91\x98\xe5\x8f\x96\xe6\xad\xa3\xe6\x96\x87\xe7\x9a\x84\xe5\x89\x8d54\xe4\xb8\xaa\xe5\xad\x97\xe7\xac\xa6', max_length=54, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=datetime.datetime(2016, 8, 8, 15, 31, 22, 201000, tzinfo=utc), verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 8, 15, 31, 35, 958000, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(default=datetime.datetime(2016, 8, 8, 15, 31, 45, 123000, tzinfo=utc), max_length=1, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'd', b'Draft'), (b'p', b'Published')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='topped',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6'),
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f'),
        ),
    ]
