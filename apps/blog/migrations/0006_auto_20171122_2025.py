# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171122_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=models.TextField(),
        ),
    ]
