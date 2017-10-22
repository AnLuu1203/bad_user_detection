# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendo', '0006_auto_20171021_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_encode', models.CharField(default='', max_length=256)),
                ('sales_order_count', models.IntegerField(default=0)),
                ('bad_user', models.BooleanField(default=False)),
                ('complete_order_count', models.IntegerField(default=0)),
                ('cancel_order_count', models.IntegerField(default=0)),
                ('close_order_count', models.IntegerField(default=0)),
                ('cancel_by_seller_count', models.IntegerField(default=0)),
                ('cancel_by_buyer_count', models.IntegerField(default=0)),
                ('seller_deny_deliver_count', models.IntegerField(default=0)),
                ('seller_request_cancel_count', models.IntegerField(default=0)),
                ('split_order_count', models.IntegerField(default=0)),
                ('combine_order_count', models.IntegerField(default=0)),
                ('cancel_by_other_count', models.IntegerField(default=0)),
                ('cancel_by_system', models.IntegerField(default=0)),
                ('continuous_order_count', models.IntegerField(default=0)),
            ],
        ),
    ]