# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(verbose_name='publication date'),
        ),
    ]
