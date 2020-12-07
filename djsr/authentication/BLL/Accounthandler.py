from ..models import Employee as EmployeeDB
from ..models import Member as MemberDB
from ..models import Membership as MembershipDB
from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import MyTokenObtainPairSerializer, AccountsSerializer , EmployeeSerializer


import json

class Register_Employee(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):

        aSerializer = AccountsSerializer(data=request.data)

        if aSerializer.is_valid():
            et = request.data.pop('Employee_Type', None)
                
            if et is None:
                return Response(aSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
            account = aSerializer.save()
            if account:
                
                eSerializer =  EmployeeDB.objects.create(Account_ID = account, Employee_Type = et)      
                
                return Response(account.id, status=status.HTTP_201_CREATED)
        
        return Response(aSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Register_Member(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        accountID = request.user.id
        approvedBy = EmployeeDB.objects.get(Account_ID = accountID)

        if approvedBy is None:
            return Response("Approved By Doesn't Exist",status=status.HTTP_400_BAD_REQUEST)

        employeeTypeObj = approvedBy._meta.get_field('Employee_Type')
        employeeType = employeeTypeObj.value_from_object(approvedBy)

        if employeeType is None:
            return Response("Employee Type Doesn't Exist",status=status.HTTP_400_BAD_REQUEST)

        if employeeType != 'PA':
            return Response("This Employee is Not Authorized to Register a Member",status=status.HTTP_400_BAD_REQUEST)

        aSerializer = AccountsSerializer(data=request.data)

        if aSerializer.is_valid():

            account = aSerializer.save()

            memSerializer = MembershipDB.objects.create(Approved_By = approvedBy)

            if memSerializer is None:
                return Response("MemberShip is Not Genrated",status=status.HTTP_400_BAD_REQUEST)

            mSerializer = MemberDB.objects.create(Account_ID = account, Membership_ID = memSerializer)

            if account:
                #json = serializer.data
                return Response(account.id, status=status.HTTP_201_CREATED)
        
        return Response(aSerializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ObtainTokenPairWithAccountsView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

