# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20171129_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
    ]
