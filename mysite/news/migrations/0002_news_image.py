# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-30 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
