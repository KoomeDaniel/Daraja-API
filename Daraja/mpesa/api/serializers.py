from rest_framework import serializers
from mpesa.models import LNMonline,C2BPayments

class LNMonlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMonline
        fields = [
            'id',
            'CheckoutRequestID',
            'MerchantRequestID',
            'ResultsCode',
            'ResultDesc',
            'Amount',
            'MpesaReceiptNumber',
            'Balance',
            'TransactionDate',
            'PhoneNumber'
        ]


class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = [
            'id',
            'TransactionType',
            'TransID',
            'TransTime',
            'TransAmount',
            'BusinessShortCode',
            'BillRefNumber',
            'InvoiceNumber',
            'OrgAccountBalance',
            'ThirdPartyTransID',
            'MSISDN',
            'FirstName',
            'MiddleName',
            'LastName',
            
        ]
