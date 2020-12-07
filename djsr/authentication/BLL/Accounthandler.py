from ..models import Employee as EmployeeDB
from ..models import Accounts as AccountDB
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

class Deregister_Member(APIView):
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
            return Response("This Employee is Not Authorized to Deregister a Member",status=status.HTTP_400_BAD_REQUEST)

        deregister_id = request.data['Member_ID']

        memberAcc = MemberDB.objects.get(Member_ID = deregister_id)

        if memberAcc is None:
            return Response("No Member exits against this MemberID",status=status.HTTP_400_BAD_REQUEST)

        membershipIdObj = memberAcc._meta.get_field('Membership_ID')
        membershipId = membershipIdObj.value_from_object(memberAcc)
        accountIdObj = memberAcc._meta.get_field('Account_ID')
        accountId = accountIdObj.value_from_object(memberAcc)

        membershipAcc = MembershipDB.objects.get(Membership_ID = membershipId)
        accountsAcc = AccountDB.objects.get(id = accountId)

        if accountsAcc is None:
            return Response("No Account is Registered against this Member",status=status.HTTP_400_BAD_REQUEST)
        if membershipAcc is None:
            return Response("No Membership found against this Member",status=status.HTTP_400_BAD_REQUEST)

        #LATER ON CHECK THAT MEMBER DONT HAVE ANY UNPAID DUES

        memberAcc.delete()
        membershipAcc.delete()
        accountsAcc.delete()      

        return Response("Member "+deregister_id+" Has Successfully Been Deleted", status=status.HTTP_201_CREATED)
        
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
