from django.contrib import admin

# Register your models here.
from mpesa.models import LNMonline,C2BPayments


class LNMonlineAdmin(admin.ModelAdmin):
    list_display = ("PhoneNumber","Amount","MpesaReceiptNumber","TransactionDate")


admin.site.register(LNMonline, LNMonlineAdmin)

class C2BPaymentsAdmin(admin.ModelAdmin):
    list_display = ("MSISDN","TransAmount","TransID","TransTime")


admin.site.register(C2BPayments, C2BPaymentsAdmin)