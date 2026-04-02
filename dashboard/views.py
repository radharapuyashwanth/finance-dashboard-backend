from django.db.models import Sum
from django.db.models.functions import TruncMonth
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from records.models import FinancialRecord


class DashboardSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role not in ['viewer', 'analyst', 'admin']:
            return Response({'detail': 'You are not authorized to access dashboard summaries.'}, status=403)

        queryset = FinancialRecord.objects.filter(is_deleted=False)

        total_income = queryset.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        total_expense = queryset.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        net_balance = total_income - total_expense

        category_wise_totals = list(
            queryset.values('category', 'type').annotate(total=Sum('amount')).order_by('category')
        )

        recent_activity = list(
            queryset.values('id', 'amount', 'type', 'category', 'date', 'notes')[:5]
        )

        monthly_trends = list(
            queryset.annotate(month=TruncMonth('date'))
            .values('month', 'type')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )

        return Response({
            'total_income': total_income,
            'total_expense': total_expense,
            'net_balance': net_balance,
            'category_wise_totals': category_wise_totals,
            'recent_activity': recent_activity,
            'monthly_trends': monthly_trends,
        })
