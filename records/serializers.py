from decimal import Decimal
from rest_framework import serializers
from .models import FinancialRecord


class FinancialRecordSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = FinancialRecord
        fields = [
            'id', 'amount', 'type', 'category', 'date', 'notes',
            'created_by', 'created_by_username', 'created_at', 'updated_at', 'is_deleted'
        ]
        read_only_fields = ['id', 'created_by', 'created_by_username', 'created_at', 'updated_at', 'is_deleted']

    def validate_amount(self, value):
        if value <= Decimal('0'):
            raise serializers.ValidationError('Amount must be greater than 0.')
        return value

    def validate_category(self, value):
        if not value.strip():
            raise serializers.ValidationError('Category cannot be empty.')
        return value.strip()
