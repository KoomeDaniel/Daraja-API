# Generated by Django 5.0.6 on 2024-06-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mpesa", "0002_lnmonline_amount_lnmonline_balance_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lnmonline",
            name="MerchantRequestID",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="lnmonline",
            name="MpesaReceiptNumber",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
