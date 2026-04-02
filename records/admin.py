from django.contrib import admin
from .models import FinancialRecord


@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'category', 'amount', 'date', 'created_by', 'is_deleted')
    list_filter = ('type', 'category', 'date', 'is_deleted')
    search_fields = ('category', 'notes', 'created_by__username')
