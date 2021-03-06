# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-06 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20180107_1257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='students',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='students',
            name='middle_name',
            field=models.CharField(blank=True, default=b'', max_length=256, verbose_name='Middle name'),
        ),
        migrations.AlterField(
            model_name='students',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='students',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Group', verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='students',
            name='ticket',
            field=models.CharField(max_length=256, verbose_name='Ticket'),
        ),
    ]
