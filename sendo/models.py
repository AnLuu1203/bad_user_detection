# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SalesOrder(models.Model):
    buyer_region_name = models.CharField(max_length=256, default='')
    buyer_district_name = models.CharField(max_length=256, default='')
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    payment_method = models.CharField(max_length=256, default='')
    carrier_service_name = models.CharField(max_length=256, default='')
    order_status = models.CharField(max_length=256, default='')
    reason_cancel = models.TextField(default='')
    buyer_phone_encode = models.CharField(max_length=256, default='')
    buyer_name_encode = models.CharField(max_length=256, default='')
    email_encode = models.CharField(max_length=256, default='')
    buyer_address_encode = models.CharField(max_length=256, default='')
    order_date = models.DateTimeField(null=True)
    order_expected_delivery_date = models.DateTimeField(null=True)
    store_id_encode = models.CharField(max_length=256, default='')
    user = models.ForeignKey('sendo.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.__dict__)

class SalesOrderDetail(models.Model):
    product_name = models.CharField(max_length=256, default='')
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.__dict__)

class Shipment(models.Model):
    shipment_date = models.DateTimeField(null=True)
    delivery_status = models.CharField(max_length=256, default='')
    delivery_status_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(null=True)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.__dict__)

class BlacklistPhone(models.Model):
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)
    phone_number_encode = models.CharField(max_length=256, default='')
    created_user_encode = models.CharField(max_length=256, default='')
    updated_user_encode = models.CharField(max_length=256, default='')

    def __str__(self):
        return str(self.__dict__)

class BlacklistHistory(models.Model):
    created_date = models.DateTimeField(null=True)
    note = models.TextField(default='')
    phone_number_encode = models.CharField(max_length=256, default='')
    store_id_encode = models.CharField(max_length=256, default='')
    blacklist_phone = models.ForeignKey(BlacklistPhone, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.__dict__)

class User(models.Model):
    phone_number_encode = models.CharField(max_length=256, default='')
    sales_order_count = models.IntegerField(default=0)
    bad_user = models.BooleanField(default=False)
    complete_order_count = models.IntegerField(default=0)
    cancel_order_count = models.IntegerField(default=0)
    close_order_count = models.IntegerField(default=0)
    cancel_by_seller_count = models.IntegerField(default=0)
    cancel_by_buyer_count = models.IntegerField(default=0)
    seller_deny_deliver_count = models.IntegerField(default=0)
    seller_request_cancel_count = models.IntegerField(default=0)
    split_order_count = models.IntegerField(default=0)
    combine_order_count = models.IntegerField(default=0)
    cancel_by_other_count = models.IntegerField(default=0)
    cancel_by_system = models.IntegerField(default=0)
    continuous_order_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.__dict__)
