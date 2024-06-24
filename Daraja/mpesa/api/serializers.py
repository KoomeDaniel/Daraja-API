from rest_framework import serializers
from mpesa.models import LNMonline

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
