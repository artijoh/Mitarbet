# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_developers'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='wiki',
            field=models.CharField(default='', max_length=100000),
            preserve_default=False,
        ),
    ]
