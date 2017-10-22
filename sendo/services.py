from __future__ import unicode_literals
from .models import *
from django.utils.dateparse import parse_datetime

import csv

class SendoDataHandler(object):
    @staticmethod
    def import_sales_orders():
        spamreader = csv.reader(open('sendo/data/sales_orders.csv', newline=''))
        for row in spamreader:
            print(row)
            row = [x.strip() for x in row]
            sales_order = SalesOrder()
            sales_order.buyer_region_name = row[0]
            sales_order.buyer_district_name = row[1]
            try:
                sales_order.total_amount = float(row[2])
            except:
                sales_order.total_amount = 0
            sales_order.payment_method = row[3]
            sales_order.carrier_service_name = row[4]
            sales_order.order_date = parse_datetime(row[5])
            sales_order.order_expected_delivery_date = parse_datetime(row[6])
            sales_order.order_status = row[7]
            sales_order.reason_cancel = row[8]
            sales_order.id = row[9].split('_').pop()
            sales_order.buyer_phone_encode = row[10]
            sales_order.buyer_name_encode = row[11]
            sales_order.email_encode = row[12]
            sales_order.buyer_address_encode = row[13]
            sales_order.store_id_encode = row[14]
            sales_order.save()

    @staticmethod
    def import_sales_order_details():
        spamreader = csv.reader(open('sendo/data/sales_order_details.csv', newline=''))
        for row in spamreader:
            print(row)
            row = [x.strip() for x in row]
            sales_order_detail = SalesOrderDetail()
            sales_order_detail.product_name = row[0]
            try:
                sales_order_detail.price = float(row[1])
            except:
                sales_order_detail.price = 0
            sales_order_detail.quantity = row[2]
            try:
                sales_order_detail.subtotal = float(row[3])
            except:
                sales_order_detail.subtotal = 0
            sales_order_detail.id = row[4].split('_').pop()
            sales_order_detail.sales_order_id = row[5].split('_').pop()
            sales_order_detail.product_variant_id_encode = row[6]
            sales_order_detail.save()

    @staticmethod
    def import_shipments():
        spamreader = csv.reader(open('sendo/data/shipments.csv', newline=''))
        for row in spamreader:
            print(row)
            row = [x.strip() for x in row]
            shipment = Shipment()
            shipment.shipment_date = parse_datetime(row[0])
            shipment.delivery_status = row[1]
            shipment.delivery_status_date = parse_datetime(row[2])
            shipment.created_date = row[3]
            shipment.id = row[4].split('_').pop()
            shipment.sales_order_id = row[5].split('_').pop()
            shipment.save()

    @staticmethod
    def import_blacklist_phones():
        spamreader = csv.reader(open('sendo/data/blacklist_phones.csv', newline=''))
        for row in spamreader:
            print(row)
            row = [x.strip() for x in row]
            blacklist_phone = BlacklistPhone()
            blacklist_phone.created_date = parse_datetime(row[0])
            blacklist_phone.updated_date = parse_datetime(row[1])
            blacklist_phone.id = row[2].split('_').pop()
            blacklist_phone.phone_number_encode = row[3]
            blacklist_phone.created_user_encode = row[4]
            blacklist_phone.updated_user_encode = row[5]
            blacklist_phone.save()

    @staticmethod
    def import_blacklist_histories():
        spamreader = csv.reader(open('sendo/data/blacklist_histories.csv', newline=''))
        for row in spamreader:
            print(row)
            row = [x.strip() for x in row]
            blacklist_history = BlacklistHistory()
            blacklist_history.created_date = parse_datetime(row[0])
            blacklist_history.note = row[1]
            blacklist_history.id = row[2].split('_').pop()
            blacklist_history.blacklist_phone_id = row[3].split('_').pop()
            blacklist_history.phone_number_encode = row[4]
            blacklist_history.store_id_encode = row[5]
            blacklist_history.save()

    @staticmethod
    def import_data():
        SendoDataHandler.delete_data()
        SendoDataHandler.import_sales_orders()
        SendoDataHandler.import_sales_order_details()
        SendoDataHandler.import_shipments()
        SendoDataHandler.import_blacklist_phones()
        SendoDataHandler.import_blacklist_histories()
        SendoDataHandler.create_users()

    @staticmethod
    def delete_data():
        print('Deleting old data....')
        [x.delete() for x in SalesOrder.objects.all()]
        [x.delete() for x in SalesOrderDetail.objects.all()]
        [x.delete() for x in Shipment.objects.all()]
        [x.delete() for x in BlacklistPhone.objects.all()]
        [x.delete() for x in BlacklistHistory.objects.all()]
        [x.delete() for x in User.objects.all()]

    @staticmethod
    def create_users():
        for sales_order in SalesOrder.objects.all():
            try:
                user = User.objects.get(phone_number_encode=sales_order.buyer_phone_encode)
            except:
                user = User(phone_number_encode=sales_order.buyer_phone_encode)
            user.save()
            sales_order.user_id = user.id
            sales_order.save()
            print(user)

        SendoDataHandler.update_users()

    @staticmethod
    def update_users():
        for user in User.objects.all():
            user.bad_user = BlacklistPhone.objects.filter(phone_number_encode=user.phone_number_encode).count() > 0

            sales_orders = SalesOrder.objects.filter(user_id=user.id)
            user.sales_order_count = sales_orders.count()
            user.complete_order_count = sales_orders.filter(order_status='Hoàn tất').count()
            user.cancel_order_count = sales_orders.filter(order_status='Hủy').count()
            user.close_order_count = sales_orders.filter(order_status='Đóng').count()

            cancel_sales_orders = sales_orders.filter(order_status='Hủy')
            user.cancel_by_seller_count = cancel_sales_orders.filter(reason_cancel='Hủy bởi Seller').count()
            user.cancel_by_buyer_count = cancel_sales_orders.filter(reason_cancel='Hủy bởi Buyer').count()
            user.seller_deny_deliver_count = cancel_sales_orders.filter(reason_cancel='Seller từ chối giao hàng').count()
            user.seller_request_cancel_count = cancel_sales_orders.filter(reason_cancel='Seller yêu cầu hủy').count()
            user.split_order_count = cancel_sales_orders.filter(reason_cancel='Hủy bởi tách đơn hàng').count()
            user.combine_order_count = cancel_sales_orders.filter(reason_cancel='Gộp đơn hàng').count()
            user.cancel_by_other_count = cancel_sales_orders.filter(reason_cancel='Hủy lý do khác').count()
            user.cancel_by_system = cancel_sales_orders.filter(reason_cancel='Hủy tự động bởi hệ thống').count()
            user.save()
            print(user)
