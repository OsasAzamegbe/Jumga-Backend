from django.contrib import admin
from .models import Transaction, Merchant

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Merchant)