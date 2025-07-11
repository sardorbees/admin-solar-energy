from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from . import serializers
from .methods_merchant_api import Services
from .models import ClickTransaction
from .status import (ORDER_FOUND, INVALID_AMOUNT, ORDER_NOT_FOUND)
from .utils import PyClickMerchantAPIView


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClickTransaction

class CreateClickTransactionView(APIView):
    def post(self, request, *args, **kwargs):
        amount = request.data.get("amount")  # <- здесь может быть None

        if amount is None:
            return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)

        order = ClickTransaction.objects.create(amount=amount)
        return Response({"status": "created", "order_id": order.id}, status=status.HTTP_201_CREATED)


class TransactionCheck(PyClickMerchantAPIView):
    @classmethod
    def check_order(cls, order_id: str, amount: str):
        if order_id:
            try:
                order = ClickTransaction.objects.get(id=order_id)
                if int(amount) == order.amount:
                    return ORDER_FOUND
                else:
                    return INVALID_AMOUNT
            except ClickTransaction.DoesNotExist:
                return ORDER_NOT_FOUND

    @classmethod
    def successfully_payment(cls, transaction: ClickTransaction):
        """ Эта функция вызывается после успешной оплаты """
        pass


class ClickTransactionTestView(PyClickMerchantAPIView):
    VALIDATE_CLASS = TransactionCheck


class ClickMerchantServiceView(APIView):
    def post(self, request, service_type, *args, **kwargs):
        service = Services(request.POST, service_type)
        response = service.api()
        return JsonResponse(response)

class ClickTransactionCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClickTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # <-- тут должно быть amount
        return Response(serializer.data)