from django.contrib import admin
from .models import CollectorNote, CustomerTransaction, PaymentPlan

# Register your models here.
admin.site.register(CollectorNote)
admin.site.register(CustomerTransaction)
admin.site.register(PaymentPlan)