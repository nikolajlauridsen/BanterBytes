# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tales.Mood')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tales.Topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
