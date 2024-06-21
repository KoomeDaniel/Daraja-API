from django.contrib import admin

# Register your models here.
from mpesa.models import LNMonline


class LNMonlineAdmin(admin.ModelAdmin):
    list_display = ("PhoneNumber","Amount","MpesaReceiptNumber","TransactionDate")


admin.site.register(LNMonline, LNMonlineAdmin)