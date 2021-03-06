# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'FIRST PLAYER TO MOVE'), ('S', 'SECOND PLAYER TO MOVE'), ('D', 'DRAW'), ('L', 'SECOND PLAYER WINS'), ('W', 'WITHDRAW')], default='F', max_length=1),
        ),
    ]
