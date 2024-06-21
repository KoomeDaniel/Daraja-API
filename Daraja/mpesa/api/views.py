from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mpesa.models import LNMonline
from mpesa.api.serializers import LNMonlineSerializer
from datetime import datetime
import pytz

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMonline.objects.all()
    serializer_class = LNMonlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            print(request.data, "This is request.data")
            
            body = request.data.get("Body", {})
            stk_callback = body.get("stkCallback", {})
            callback_metadata = stk_callback.get("CallbackMetaData", {})
            items = callback_metadata.get("Item", [])

            # Initialize variables with default values
            merchant_request_id = stk_callback.get("MerchantRequestID", "N/A")
            print(merchant_request_id, "this should be MerchantRequestID")
            checkout_request_id = stk_callback.get("CheckoutRequestID", "N/A")
            result_code = stk_callback.get("ResultCode", "N/A")
            result_description = stk_callback.get("ResultDesc", "N/A")
            amount = "N/A"
            mpesa_receipt_number = "N/A"
            balance = ""
            transaction_date = "N/A"
            phone_number = "N/A"

            # Safely extract values from items
            for item in items:
                key = item.get("key")
                value = item.get("value")
                if key == "Amount":
                    amount = value
                elif key == "MpesaReceiptNumber":
                    mpesa_receipt_number = value
                elif key == "TransactionDate":
                    transaction_date = value
                elif key == "PhoneNumber":
                    phone_number = value

            print(amount, "This should be amount")

            # Convert transaction date to datetime object
            if transaction_date != "N/A":
                str_transaction_date = str(transaction_date)
                print(str_transaction_date, "this should be str_transaction_date")
                transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
                aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
                print(aware_transaction_datetime, "This should be a transaction_datetime")
            else:
                aware_transaction_datetime = None

            # Create or update LNMonline instance
            lnmonline, created = LNMonline.objects.get_or_create(
                MpesaReceiptNumber=mpesa_receipt_number,
                defaults={
                    "CheckoutRequestID": checkout_request_id,
                    "MerchantRequestID": merchant_request_id,
                    "ResultsCode": result_code,
                    "ResultDesc": result_description,
                    "Amount": amount,
                    "Balance": balance,
                    "TransactionDate": aware_transaction_datetime,
                    "PhoneNumber": phone_number,
                }
            )

            # Log the creation status
            if created:
                print(f"New LNMonline instance created: {lnmonline}")
            else:
                print(f"Existing LNMonline instance updated: {lnmonline}")

            return Response({"OurRequestDesc": "YEEY!!! It worked"})

        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({"error": str(e)}, status=400)
