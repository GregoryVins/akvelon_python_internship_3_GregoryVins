from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

import transactions
from custom_user.views import CustomUserViewSet
from transactions.views import TransactionViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/profit/', transactions.views.profit),
    path('api/doc/', get_swagger_view(title='REST API Document'))
]
