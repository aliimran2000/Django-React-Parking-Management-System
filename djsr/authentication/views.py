# djsr/authentication/views.py
from django.contrib.auth.models import Group
#from .models import Accounts
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MyTokenObtainPairSerializer, AccountsSerializer , EmployeeSerializer

class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AccountsCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = AccountsSerializer(data=request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            if account:
                json = serializer.data
                return Response(account.id, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request,format='json'):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            emp = serializer.save()
            if emp:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






       