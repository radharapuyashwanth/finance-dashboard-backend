from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserViewSet
from records.views import RecordViewSet
from dashboard.views import DashboardSummaryAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'records', RecordViewSet, basename='records')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/dashboard/summary/', DashboardSummaryAPIView.as_view(), name='dashboard-summary'),
    path('api/', include(router.urls)),
]
