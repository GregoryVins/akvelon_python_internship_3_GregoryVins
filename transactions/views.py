from rest_framework.viewsets import ModelViewSet

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.request.GET.get("userId")
        if user_id:
            return Transaction.objects.filter(user__id=user_id)
        return Transaction.objects.all()
