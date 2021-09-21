from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    """
    list:
    Get all transactions.
    If you want to get all user's transactions,
    you can send user id (uuid: str) as param in URL request.

    example url
    http://127.0.0.1:8000/api/transactions/?userId=d0c509da-c336-49fc-9ba1-e5834a06d8cc

    """
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.request.GET.get("userId")
        if user_id:
            return Transaction.objects.filter(user__id=user_id)
        return Transaction.objects.all()


class ProfitAPIView(APIView):
    """
    User's profit per day
    ---------------------
    `userId: str` - *required param. You have to send user uuid

    *Example value:*

        {
          "userId": "d0c509da-c336-49fc-9ba1-e5834a06d8cc"
        }

    If you want to receive data for some period, then you have to complete
    the required parameters with date of start and end.

    `date_start: str` - Date of start

    `date_finish: str` - Date of finish

    *For example:*

        {
          "userId": "d0c509da-c336-49fc-9ba1-e5834a06d8cc",
          "date_start": "2021-09-17",
          "date_finish": "2021-09-20"
        }

    For instance, response:

        [
            {
                "date": "21-09-10",
                "sum": 177531
            },
            {
                "date": "21-09-11",
                "sum": 437278
            }
        ]
    """

    @staticmethod
    def post(request):
        user_id = request.data.get("userId", None)
        date_start = request.data.get('date_start', None)
        date_finish = request.data.get('date_finish', None)
        if user_id:
            if date_start and date_finish:
                transactions = Transaction.objects.filter(date__range=[date_start, date_finish],
                                                          user_id=user_id).order_by('date')
            else:
                transactions = Transaction.objects.filter(user_id=user_id).order_by('date')
            try:
                data = {}
                result = []
                for item in transactions:
                    data[item.date.strftime('%y-%m-%d')] = item.amount

                for key, value in data.items():  # create readable data
                    result.append(dict(date=key, sum=value))  # added profit per day in result array

                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
        return Response(dict(status='Failed. You have to send correct data'),
                        status=status.HTTP_403_FORBIDDEN)
