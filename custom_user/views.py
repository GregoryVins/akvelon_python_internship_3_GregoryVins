from rest_framework.viewsets import ModelViewSet

from custom_user.models import CustomUser
from custom_user.serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
