import logging
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mpesa.models import LNMonline
from mpesa.api.serializers import LNMonlineSerializer
from datetime import datetime
import pytz

logger = logging.getLogger(__name__)

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMonline.objects.all()
    serializer_class = LNMonlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            logger.info("Received callback data: %s", request.data)
            body = request.data.get("Body", {})
            stk_callback = body.get("stkCallback", {})
            callback_metadata = stk_callback.get("CallbackMetadata", {})
            items = callback_metadata.get("Item", [])

            # Initialize variables with default values
            merchant_request_id = stk_callback.get("MerchantRequestID", "N/A")
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
                key = item.get("Name")
                value = item.get("Value")
                if key == "Amount":
                    amount = value
                elif key == "MpesaReceiptNumber":
                    mpesa_receipt_number = value
                elif key == "TransactionDate":
                    transaction_date = value
                elif key == "PhoneNumber":
                    phone_number = value

            if transaction_date != "N/A":
                str_transaction_date = str(transaction_date)
                transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
                aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
            else:
                aware_transaction_datetime = None

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

            if created:
                logger.info("New LNMonline instance created: %s", lnmonline)
            else:
                logger.info("Existing LNMonline instance updated: %s", lnmonline)

            return Response({"OurRequestDesc": "YEEY!!! It worked"})

        except Exception as e:
            logger.error("Error processing callback: %s", str(e))
            return Response({"error": str(e)}, status=400)
