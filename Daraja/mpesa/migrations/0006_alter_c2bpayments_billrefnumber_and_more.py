# Generated by Django 4.2.4 on 2024-06-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mpesa", "0005_alter_c2bpayments_transamount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="c2bpayments",
            name="BillRefNumber",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="BusinessShortCode",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="FirstName",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="LastName",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="MSISDN",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="MiddleName",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="OrgAccountBalance",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="TransAmount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="TransID",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="TransTime",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="c2bpayments",
            name="TransactionType",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
