from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from custom_user.views import CustomUserViewSet
from transactions.views import TransactionViewSet, ProfitAPIView

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('transactions', TransactionViewSet, basename='transactions')

schema_view = get_swagger_view(title='REST API Document')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/profit/', ProfitAPIView.as_view()),
    path('api/doc/', schema_view)
]
