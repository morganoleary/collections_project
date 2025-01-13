from django.db import models

# Create your models here.
class CollectorNote(models.Model):
    note = models.CharField(max_length=255)

    def __str__(self):
        return f"Note: {self.note}"

class CustomerTransaction(models.Model):
    account_id = models.IntegerField()
    transaction_date = models.DateField()
    monthly_amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Transaction # {self.id} - Account # {self.account_id}"

class PaymentPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Plan: {self.plan_name}"