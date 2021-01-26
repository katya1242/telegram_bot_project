# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import requests
import telebot
from bot.models import *
import datetime

class Command(BaseCommand):
    help = 'Test'

    def handle(self, *args, **options):
        bot_id = '1308591822:AAFghKn_dOJaME7P82ohf6TjfHOLP72Xo_A'
        bot = telebot.TeleBot(bot_id)
        messages = Message.objects.filter(is_sent=False)
        subscribers = Subscriber.objects.all()
        for message in messages:
            for subscriber in subscribers:
                bot.send_message(subscriber.telegram_id, message.message_text)
            message.is_sent = True
            message.time_sent = datetime.datetime.now()
            message.save()




