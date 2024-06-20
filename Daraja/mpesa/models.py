from django.db import models

# Create your models here.

class LNMonline(models.Model):
    CheckoutRequestID = models.CharField(max_length=50,blank=True,null=True)
    MerchantRequestID = models.CharField(max_length=20,blank=True,null=True)
    ResultsCode = models.IntegerField(blank=True,null=True)
    ResultDesc = models.CharField(max_length=120,blank=True,null=True)
    Amount = models.FloatField(default=0,blank=True,null=True)
    MpesaReceiptNumber = models.CharField(max_length=15,blank=True,null=True)
    Balance = models.CharField(max_length=12,blank=True,null=True)
    TransactionDate = models.DateField(blank=True,null=True)
    PhoneNumber = models.CharField(max_length=15,blank=True,null=True)