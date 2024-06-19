from django.db import models

# Create your models here.

class LNMonline(models.Model):
    CheckoutRequestID = models.CharField(max_length=50)
    MerchantRequestID = models.CharField(max_length=20)
    ResultsCode = models.IntegerField
    ResultDesc = models.CharField(max_length=120)
    Amount = models.FloatField
    MpesaReceiptNumber = models.CharField(max_length=15)
    Balance = models.CharField(max_length=12,blank=True,null=True)
    TransactionDate = models.DateField
    PhoneNumber = models.CharField(max_length=15)