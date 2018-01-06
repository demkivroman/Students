# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20171130_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u041c\u0456\u0441\u044f\u0447\u043d\u0438\u0439 \u0416\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u041c\u0456\u0441\u044f\u0447\u043d\u0456 \u0436\u0443\u0440\u043d\u0430\u043b\u0438',
            },
        ),
        migrations.AlterField(
            model_name='exams',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430'),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430'),
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Students', unique_for_month='date', verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442'),
        ),
    ]
