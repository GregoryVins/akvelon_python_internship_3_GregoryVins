from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(['GET'])
def profit(request):
    start = request.query_params.get("start", False)
    finish = request.query_params.get("finish", False)
    user_id = request.query_params.get("userId", None)
    if start and finish and user_id:
        try:
            transactions = Transaction.objects.filter(date__range=[start, finish], user_id=user_id)
            total = 0
            for item in transactions:
                total += item.amount
            data = dict(start=start, finish=finish, user_id=user_id, profit=total)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            pass
    return Response(dict(status='Failed. You have to send correct data'),
                    status=status.HTTP_403_FORBIDDEN)
