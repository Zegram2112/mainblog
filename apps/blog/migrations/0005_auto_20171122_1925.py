# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 22:25
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171114_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
