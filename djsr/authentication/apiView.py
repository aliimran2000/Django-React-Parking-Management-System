from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .modelManager import MyTokenObtainPairSerializer

from .BLL.MemberManager import MemberManager
from .BLL.MembershipManager import MembershipManager
from .BLL.EmployeeManager import EmployeeManager
from .BLL.BillingManager import BillingManager

#GLOBAL VARIABLES
MemberMan = MemberManager()
MembershipMan = MembershipManager()
BillingMan = BillingManager()
EmployeeMan = EmployeeManager()

def initializeManagers():

    MemberMan.initializeManagers(MembershipMan)
    MembershipMan.initializeManagers(BillingMan)

class ObtainTokenPairWithAccountsView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class registerMemberApiView(APIView):

    #IMPLEMENT REGISTER MEMBER VIEW IN FRONTEND OF ADMIN
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        DateOfBirth = request.data['DateOfBirth']
        Cnic = request.data['CNIC']
        Address = request.data['Address']
        Phone_No = request.data['Phone_No']
        Approved_By = request.data.id

        MemberMan.registerMember(email, username, password, DateOfBirth, Cnic, Address, Phone_No, Approved_By)

        return Response("Member has been Successfully Registered", status=status.HTTP_201_CREATED)

class deregisterMemberApiView(APIView):

    #IMPLEMENT DEREGISTER MEMBER VIEW IN FRONTEND OF ADMIN
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):

        memberId = request.data['Member_ID']

        resp = MemberMan.deregisterMember(memberId)

        if resp == "Fail":
            return Response("Member "+ memberId +" has uncleared dues. Unable to deregister member", status=status.HTTP_402_PAYMENT_REQUIRED)
        else:
            return Response("Member "+ memberId +" Has Successfully Been deregistered", status=status.HTTP_201_CREATED)

class registerEmployeeApiView(APIView):

    #IMPLEMENT REGISTER EMPLOYEE VIEW IN FRONTEND OF ADMIN
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):

        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        DateOfBirth = request.data['DateOfBirth']
        Cnic = request.data['CNIC']
        Address = request.data['Address']
        Phone_No = request.data['Phone_No']
        Employee_Type = request.data['Employee_Type']

        EmployeeMan.registerEmployee(email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type)

        return Response("Employee of Type " + Employee_Type + " has successfully been registered", status=status.HTTP_201_CREATED)