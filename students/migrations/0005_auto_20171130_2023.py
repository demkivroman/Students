# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_exams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exams',
            name='groups',
            field=models.ManyToManyField(to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0438'),
        ),
    ]
