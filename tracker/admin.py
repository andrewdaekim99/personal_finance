from django.contrib import admin
from .models import Category, Transaction, TransactionAdmin


admin.site.register(Category)
admin.site.register(Transaction, TransactionAdmin)


