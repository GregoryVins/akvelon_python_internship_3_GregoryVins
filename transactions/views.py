from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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


class ProfitAPIView(APIView):
    """
    This text is the description for this API
        ---
        userId -- You have to send user id
        start -- Single date or start date, ex. "2021-09-01"
        finish -- Finish date
    """

    @staticmethod
    def post(request):
        start = request.data.get("start", False)
        finish = request.data.get("finish", False)
        user_id = request.data.get("userId", None)
        if start and user_id:
            if not finish:
                finish = start
            try:
                transactions = Transaction.objects.filter(date__range=[start, finish], user_id=user_id)
                total = 0
                for item in transactions:
                    total += item.amount
                data = dict(start=start, finish=finish, user_id=user_id, profit=total)
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                print('\nerror\nerror\n', repr(e))
        return Response(dict(status='Failed. You have to send correct data'),
                        status=status.HTTP_403_FORBIDDEN)
