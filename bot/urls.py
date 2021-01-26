from django.urls import path
from .views import SubscribersList, MessageList, MessageCreate, MessageRUD, message_list, message_add, get_message, \
    update_message, delete_message

urlpatterns = [
    path('subscribers/list/', SubscribersList.as_view()),
    path('message/list/', MessageList.as_view()),
    path('message/add/', MessageCreate.as_view()),
    path('message/<int:pk>/', MessageRUD.as_view()),
    path('message/custom/list/', message_list),
    path('message/custom/add/', message_add),
    path('message/custom/get/<int:message_id>/', get_message),
    path('message/custom/update/<int:message_id>/', update_message),
    path('message/custom/delete/<int:message_id>/', delete_message)
]