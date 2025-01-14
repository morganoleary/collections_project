from datetime import date
from django.db import models

# Create your models here.
class CollectorNote(models.Model):
    note_title = models.CharField(max_length=50)
    note_date = models.DateTimeField(default=date.today)
    note = models.CharField(max_length=255)

    class Meta:
        db_table = 'collector_notes'

    def __str__(self):
        return f"Title: {self.note_title}, Note : {self.note}, Date of Entry: {self.note_date}"

class CustomerTransaction(models.Model):
    account_id = models.IntegerField()
    transaction_date = models.DateField()
    monthly_amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'customer_transactions'

    def __str__(self):
        return f"Transaction # {self.id} - Account # {self.account_id}"

class PaymentPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'payment_plans'

    def __str__(self):
        return f"Plan: {self.plan_name}"