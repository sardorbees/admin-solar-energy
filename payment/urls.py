# urls.py
from django.urls import path
from .views import ClickPaymentCreateView, ClickWebhookView

urlpatterns = [
    path('api/click-pay/', ClickPaymentCreateView.as_view(), name='click-payment-create'),
    path('api/payment/api/click-webhook/', ClickWebhookView.as_view()),
]
