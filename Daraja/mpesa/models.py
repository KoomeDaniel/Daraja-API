from django.db import models

class LNMonline(models.Model):
    CheckoutRequestID = models.CharField(max_length=50, blank=True, null=True)
    MerchantRequestID = models.CharField(max_length=50, blank=True, null=True)
    ResultsCode = models.IntegerField(blank=True, null=True)
    ResultDesc = models.CharField(max_length=120, blank=True, null=True)
    Amount = models.FloatField(default=0, blank=True, null=True)
    MpesaReceiptNumber = models.CharField(max_length=20, blank=True, null=True)
    Balance = models.CharField(max_length=12, blank=True, null=True)
    TransactionDate = models.DateField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.PhoneNumber} HAS SENT {self.Amount} >>> {self.MpesaReceiptNumber}"

class C2BPayments(models.Model):
        TransactionType = models.CharField(max_length=50, blank=True, null=True)
        TransID = models.CharField(max_length=20, blank=True, null=True)
        TransTime = models.DateTimeField(blank=True, null=True)
        TransAmount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        BusinessShortCode = models.CharField(max_length=20, blank=True, null=True)
        BillRefNumber = models.CharField(max_length=50, blank=True, null=True)
        InvoiceNumber = models.CharField(max_length=50, blank=True, null=True)
        OrgAccountBalance = models.CharField(max_length=20, blank=True, null=True)
        ThirdPartyTransID = models.CharField(max_length=20, blank=True, null=True)
        MSISDN = models.CharField(max_length=15, blank=True, null=True)
        FirstName = models.CharField(max_length=30, blank=True, null=True)
        MiddleName = models.CharField(max_length=30, blank=True, null=True)
        LastName = models.CharField(max_length=30, blank=True, null=True)
    
        def __str__(self):
            return f"{self.MSISDN} HAS SENT {self.TransAmount} >>> {self.TransID}"