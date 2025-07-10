# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClickPayment
from .serializers import ClickPaymentSerializer
import hashlib
import requests

MERCHANT_ID = 'your_merchant_id'
SERVICE_ID = 'your_service_id'
SECRET_KEY = 'your_secret_key'

class ClickPaymentCreateView(APIView):
    def post(self, request):
        serializer = ClickPaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()

            amount = str(int(payment.amount))
            transaction_param = str(payment.id)
            return_url = 'https://premium-dez.vercel.app/payment-success'

            sign_string = f"{MERCHANT_ID}{SERVICE_ID}{SECRET_KEY}{amount}{transaction_param}"
            sign = hashlib.md5(sign_string.encode()).hexdigest()

            payment_url = (
                f"https://my.click.uz/pay?"
                f"service_id={SERVICE_ID}&merchant_id={MERCHANT_ID}"
                f"&amount={amount}&transaction_param={transaction_param}"
                f"&return_url={return_url}&sign_time={sign}"
            )

            return Response({'payment_url': payment_url})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_telegram_message(text):
    TOKEN = "ваш_bot_token"
    CHAT_ID = "ваш_chat_id"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    send_telegram_message(f"🧾 Новый заказ на оплату:\nИмя: {payment.full_name}\nСумма: {payment.amount} UZS")


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ClickWebhookView(APIView):
    def post(self, request):
        # Проверь request.data
        print("Webhook данные:", request.data)

        # Здесь можно сделать валидацию click_trans_id и прочих полей
        return Response({'status': 'success'}, status=status.HTTP_200_OK)


class ClickPayView(APIView):
    def post(self, request):
        # Здесь создаём объект оплаты и собираем URL Click
        amount = request.data.get('amount')
        order_id = 123  # сгенерировать ID из базы
        sign_string = hashlib.md5(...).hexdigest()

        payment_url = f"https://my.click.uz/pay?service_id=...&merchant_id=...&amount={amount}&transaction_param={order_id}&sign_time={sign_string}&return_url=https://ваш-сайт.уз/success"

        return Response({'payment_url': payment_url})