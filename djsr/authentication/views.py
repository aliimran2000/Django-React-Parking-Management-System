# djsr/authentication/views.py
from .models import Accounts
from .models import Employee as EmployeeDB
from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MyTokenObtainPairSerializer, AccountsSerializer , EmployeeSerializer

import json

class Register_Employee(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):

        aSerializer = AccountsSerializer(data=request.data)

        if aSerializer.is_valid():
            account = aSerializer.save()
            if account:
                eT = request.data.pop('Employee_Type', None)

                eSerializer =  EmployeeDB.objects.create(Account_ID = account, Employee_Type = eT)      

                #if not eSerializer.is_valid():
                #    return Response(eSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

                #json = serializer.data
                return Response(account.id, status=status.HTTP_201_CREATED)
        
        return Response(aSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Register_Member(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):
        
        serializer = AccountsSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            if account:
                #json = serializer.data
                return Response(account.id, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainTokenPairWithAccountsView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
