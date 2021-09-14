from django.contrib import admin

from transactions.models import Transaction


@admin.register(Transaction)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'date')
    list_filter = ('date', )
