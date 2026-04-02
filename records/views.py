from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from .models import FinancialRecord
from .permissions import RecordAccessPermission
from .serializers import FinancialRecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialRecordSerializer
    permission_classes = [RecordAccessPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['category', 'notes', 'type']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_queryset(self):
        queryset = FinancialRecord.objects.filter(is_deleted=False)

        record_type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if record_type:
            queryset = queryset.filter(type=record_type)
        if category:
            queryset = queryset.filter(category__iexact=category)
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save(update_fields=['is_deleted'])
        return Response({'detail': 'Record soft deleted successfully.'}, status=status.HTTP_200_OK)
