# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-08 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20170827_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='magic',
            field=models.CharField(blank=True, choices=[('red', 'Red'), ('green', 'Green'), ('teal', 'Teal'), ('blue', 'Blue'), ('purple', 'Purple'), ('orange', 'Orange'), ('grey', 'Grey')], max_length=18, verbose_name='magic'),
        ),
    ]