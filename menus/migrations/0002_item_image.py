# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-25 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.URLField(default='http://col21-delagrange-liernais.ac-dijon.fr/wp-content/uploads/2018/05/cantine-2.jpg'),
        ),
    ]