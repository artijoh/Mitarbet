# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 17:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='developers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]