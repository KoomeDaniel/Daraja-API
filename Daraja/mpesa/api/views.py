import logging
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mpesa.models import LNMonline,C2BPayments
from mpesa.api.serializers import LNMonlineSerializer,C2BPaymentSerializer
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


class C2BValidationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            logger.info("Received request.data in Validation: %s", request.data)
            
            # Extract necessary fields from the request data
            transaction_type = request.data.get("TransactionType", "")
            trans_id = request.data.get("TransID", "")
            trans_time = request.data.get("TransTime", "")
            trans_amount = request.data.get("TransAmount", "")
            business_short_code = request.data.get("BusinessShortCode", "")
            bill_ref_number = request.data.get("BillRefNumber", "")
            invoice_number = request.data.get("InvoiceNumber", "")
            org_account_balance = request.data.get("OrgAccountBalance", "")
            third_party_trans_id = request.data.get("ThirdPartyTransID", "")
            msisdn = request.data.get("MSISDN", "")
            first_name = request.data.get("FirstName", "")
            middle_name = request.data.get("MiddleName", "")
            last_name = request.data.get("LastName", "")

            # Parse the transaction date and time
            trans_datetime = datetime.strptime(trans_time, "%Y%m%d%H%M%S")
            aware_trans_datetime = pytz.utc.localize(trans_datetime)

            # Create a new C2BPayments object
            c2b_payment = C2BPayments.objects.create(
                TransactionType=transaction_type,
                TransID=trans_id,
                TransTime=aware_trans_datetime,
                TransAmount=trans_amount,
                BusinessShortCode=business_short_code,
                BillRefNumber=bill_ref_number,
                InvoiceNumber=invoice_number,
                OrgAccountBalance=org_account_balance,
                ThirdPartyTransID=third_party_trans_id,
                MSISDN=msisdn,
                FirstName=first_name,
                MiddleName=middle_name,
                LastName=last_name,
            )

            logger.info("New C2BPayments instance created: %s", c2b_payment)

            return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

        except Exception as e:
            logger.error("Error processing callback: %s", str(e))
            return Response({"ResultCode": 1, "ResultDesc": str(e)}, status=400)


class C2BConfirmationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            logger.info("Received request.data in Confirmation: %s", request.data)
            
            # Extract necessary fields from the request data
            transaction_type = request.data.get("TransactionType", "")
            trans_id = request.data.get("TransID", "")
            trans_time = request.data.get("TransTime", "")
            trans_amount = request.data.get("TransAmount", "")
            business_short_code = request.data.get("BusinessShortCode", "")
            bill_ref_number = request.data.get("BillRefNumber", "")
            invoice_number = request.data.get("InvoiceNumber", "")
            org_account_balance = request.data.get("OrgAccountBalance", "")
            third_party_trans_id = request.data.get("ThirdPartyTransID", "")
            msisdn = request.data.get("MSISDN", "")
            first_name = request.data.get("FirstName", "")
            middle_name = request.data.get("MiddleName", "")
            last_name = request.data.get("LastName", "")

            # Parse the transaction date and time
            trans_datetime = datetime.strptime(trans_time, "%Y%m%d%H%M%S")
            aware_trans_datetime = pytz.utc.localize(trans_datetime)

            # Create a new C2BPayments object
            c2b_payment = C2BPayments.objects.create(
                TransactionType=transaction_type,
                TransID=trans_id,
                TransTime=aware_trans_datetime,
                TransAmount=trans_amount,
                BusinessShortCode=business_short_code,
                BillRefNumber=bill_ref_number,
                InvoiceNumber=invoice_number,
                OrgAccountBalance=org_account_balance,
                ThirdPartyTransID=third_party_trans_id,
                MSISDN=msisdn,
                FirstName=first_name,
                MiddleName=middle_name,
                LastName=last_name,
            )

            logger.info("New C2BPayments instance created: %s", c2b_payment)

            return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

        except Exception as e:
            logger.error("Error processing callback: %s", str(e))
            return Response({"ResultCode": 1, "ResultDesc": str(e)}, status=400)
