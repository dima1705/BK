from __future__ import absolute_import, unicode_literals

from django.core.mail import send_mail
from django.conf import settings
from .models import Order, OrderItem
from celery import shared_task


@shared_task()
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    # order_items = OrderItem.objects.get(id=order_id)
    subject = f'Подтверждение заказа'
    message = f'Здравствуйте {order.first_name}! Ваш заказ №{order.id} подтвержден! Мы сообщим вам, как только повар приготовит ваш заказ.'
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email])
    return mail_sent

