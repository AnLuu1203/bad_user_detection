# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sendo', '0004_shipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(null=True)),
                ('note', models.TextField(default='')),
                ('phone_number_encode', models.CharField(default='', max_length=256)),
                ('store_id_encode', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BlacklistPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('phone_number_encode', models.CharField(default='', max_length=256)),
                ('created_user_encode', models.CharField(default='', max_length=256)),
                ('updated_user_encode', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='blacklisthistory',
            name='blacklist_phone_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sendo.BlacklistPhone'),
        ),
    ]