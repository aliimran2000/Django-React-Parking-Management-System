from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .modelManager import MyTokenObtainPairSerializer
from .modelManager import getAccountName, getAccountType, isMemberCredentialValid

from .BLL.MemberManager import MemberManager
from .BLL.MembershipManager import MembershipManager
from .BLL.EmployeeManager import EmployeeManager
from .BLL.BillingManager import BillingManager
from .BLL.VehicleManager import VehicleManager
from .BLL.ParkingLotManager import ParkingLotManager
from .BLL.PaymentManager import PaymentManager

#GLOBAL VARIABLES
MemberMan = MemberManager()
MembershipMan = MembershipManager()
BillingMan = BillingManager()
EmployeeMan = EmployeeManager()
VehicleMan = VehicleManager()
ParkingLotMan = ParkingLotManager()
PaymentMan = PaymentManager()

def initializeManagers():

    MemberMan.initializeManagers(MembershipMan, VehicleMan)
    MembershipMan.initializeManagers(BillingMan)
    VehicleMan.initializeManagers(BillingMan, MemberMan)
    ParkingLotMan.initializeManagers(MemberMan, BillingMan, VehicleMan)
    BillingMan.initializeManagers(MemberMan, MembershipMan)

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

class verifyCredentialsApiView(APIView):

    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):

        username = request.data['username']
        password = request.data['password']
        
        memberId = isMemberCredentialValid(username, password)

        if (memberId != None):
            return Response(str(memberId), status=status.HTTP_200_OK)
        else:
            return Response("INVALD", status=status.HTTP_401_UNAUTHORIZED)

class registerMemberApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        DateOfBirth = request.data['DateOfBirth']
        Cnic = request.data['CNIC']
        Address = request.data['Address']
        Phone_No = request.data['Phone_No']
        Approved_By = request.user.id

        MemberMan.registerMember(email, username, password, DateOfBirth, Cnic, Address, Phone_No, Approved_By)

        return Response("Member has been Successfully Registered", status=status.HTTP_201_CREATED)

class deregisterMemberApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        memberId = request.data['Member_ID']

        resp = MemberMan.deregisterMember(memberId)

        if resp == "Fail":
            return Response("Member "+ str(memberId) +" has uncleared dues. Unable to deregister member", status=status.HTTP_402_PAYMENT_REQUIRED)
        else:
            return Response("Member "+ str(memberId) +" Has Successfully Been deregistered", status=status.HTTP_201_CREATED)

class renewMembershipApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        memberId = request.data['Member_ID']

        Approved_By = request.user.id

        resp = MemberMan.renewMembership(memberId, Approved_By)

        if resp == "Not Expired":
            return Response("Member ID : "+ str(memberId) +"'s Membership has not yet expired, hence, unable to renew membership", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response("Member ID :"+ str(memberId) +" Membership Has Successfully Been Renewed", status=status.HTTP_201_CREATED)


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

        return Response("Employee of Type " + str(Employee_Type) + " has successfully been registered", status=status.HTTP_201_CREATED)

class registerVehicleApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        Vehicle_ID = request.data['Vehicle_ID']        
        Member_ID = request.data['Member_ID']
        Vehicle_Model = request.data['Vehicle_Model']

        MemberMan.registerVehicle(Vehicle_ID, Member_ID, Vehicle_Model)

        return Response("Vehicle " + str(Vehicle_ID) + " has successfully been registered against Member " + str(Member_ID), status=status.HTTP_201_CREATED)

class deregisterVehicleApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        Member_ID = request.data['Member_ID']
        Vehicle_ID = request.data['Vehicle_ID']

        ret = VehicleMan.deregisterVehicle(Member_ID, Vehicle_ID)

        if ret == "401":
            return Response("Vehicle " + str(Vehicle_ID) + " is not Registered with Member " + Member_ID, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("Vehicle " + str(Vehicle_ID) + " has successfully been deregistered", status=status.HTTP_200_OK)

class parkVehicleApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        Vehicle_ID = request.data['Vehicle_ID']
        Member_ID = request.data['Member_ID']

        slot = ParkingLotMan.parkVehicle(Member_ID, Vehicle_ID)

        if slot == "EXPIRED":
            return Response("Member " + str(Member_ID) + " Membership has been expired, please renew it", status=status.HTTP_406_NOT_ACCEPTABLE)
        elif slot == "NOT REGISTERED":
            return Response("Vehicle " + str(Vehicle_ID) + " is not registered against this Member", status=status.HTTP_401_UNAUTHORIZED)
        elif slot == "UNCLEARED DUES":
            return Response("Member " + str(Member_ID) + " has uncleared overdue bills, please pay bill", status=status.HTTP_402_PAYMENT_REQUIRED)            
        elif slot == "PARKING FULL":
            return Response("Parking is Full", status=status.HTTP_306_RESERVED)
        else:
            return Response(str(slot) , status=status.HTTP_200_OK)

class exitVehicleApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        Vehicle_ID = request.data['Vehicle_ID']
        Member_ID = request.data['Member_ID']

        fees = ParkingLotMan.exitVehicle(Member_ID, Vehicle_ID)

        if fees == "NOT REGISTERED":
            return Response("Vehicle " + str(Vehicle_ID) + " is not registered against this Member", status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(str(fees) , status=status.HTTP_200_OK)    

class accountTypeApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        accountId = request.user.id
 
        type = getAccountType(accountId)

        return Response(str(type), status.HTTP_200_OK)

class accountNameApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        accountId = request.user.id
        name = getAccountName(accountId)
        return Response(name, status.HTTP_200_OK)

class memberDetailsApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        memberId = request.data['Member_ID']

        memberDetails = MemberMan.getMemberDetails(memberId)
    
        return Response(memberDetails, status.HTTP_200_OK)

class getVehiclesDetailApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        memberId = request.data['Member_ID']

        vehiclesDetail = VehicleMan.getVehiclesDetail(memberId)
    
        if vehiclesDetail is None:
            return Response("No Vehicle is Registered Against Member " + str(memberId), status.HTTP_404_NOT_FOUND)
        else:
            return Response(vehiclesDetail, status.HTTP_200_OK)

class getBillsDetailApiView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format='json'):

        memberId = request.data['Member_ID']

        billsDetail = BillingMan.getBillsDetail(memberId)
    
        if billsDetail is None:
            return Response("No Bill is present Against Member " + str(memberId), status.HTTP_404_NOT_FOUND)
        else:
            return Response(billsDetail, status.HTTP_200_OK)
