# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-26 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliss', '0019_claim_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='last_edited',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='last_edited',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
