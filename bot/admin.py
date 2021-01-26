from django.contrib import admin
from .models import *

@admin.register(Subscriber)
class Subscriberadmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'username',
        'telegram_id'
    ]

@admin.register(Message)
class Messageadmin(admin.ModelAdmin):
    list_display = [
        'id',
        'time_sent',
        'is_sent',
        'message_text'
        ]

