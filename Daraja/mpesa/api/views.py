from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from mpesa.models import LNMonline
from mpesa.api.serializers import LNMonlineSerializer

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMonline.objects.all()
    serializer_class = LNMonlineSerializer
    permission_classes = [AllowAny]

    def create(self,request):
        print(request.data,"This is request.data")
        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id,"this should be MerchantRequestID")
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        Result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        Result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetaData"]["Item"][0]["value"]
        print(amount,"This is should be amount")
        MpesaReceiptNumber =  request.data["Body"]["stkCallback"]["CallbackMetaData"]["Item"][1]["value"]
        balance =""
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetaData"]["Item"][3]["value"]
        phone_number = request.data["Body"]["stkCallback"]["CallbackMetaData"]["Item"][4]["value"]

        from datetime import datetime
        str_transaction_date = str(transaction_date)

        print(str_transaction_date,"this should be str_transaction_date")
        transaction_datetime = datetime.strptime(str_transaction_date,"%Y%m%d%H%M%S")
        print(transaction_datetime,"This should be a transaction_datetime")
        import pytz
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        print(transaction_datetime,"This should be a transaction_datetime")

        from mpesa.models import LNMonline
        our_model = LNMonline.objects.create(
            CheckoutRequestID = checkout_request_id,
            MerchantRequestID = merchant_request_id,
            ResultsCode = Result_code,
            ResultDesc = Result_description,
            Amount = amount,
            MpesaReceiptNumber = MpesaReceiptNumber,
            Balance = balance,
            TransactionDate = aware_transaction_datetime,
            PhoneNumber = phone_number,
        )
        our_model.save()
        from rest_framework.response import Response
        return Response ({"OurRequestDesc": "YEEY!!! It worked"})
