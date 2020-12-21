from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Employee as EmployeeDB
from .models import Accounts as AccountDB
from .models import Member as MemberDB
from .models import Membership as MembershipDB
from .models import Bill as BillDB
from .models import Vehicle as VehicleDB

from rest_framework.response import Response
from rest_framework import status, permissions

from django.utils import timezone

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        return token

def EmployeeSerializer(Email, Username, Password, Dob, Cnic, Address, PhoneNo, EmployeeType):

    account = AccountDB.objects.create(email = Email, username = Username, password = Password, DateOfBirth = Dob , CNIC = Cnic, Address = Address, Phone_No = PhoneNo)
    account.set_password(Password)
    account.save()
    return EmployeeDB.objects.create(Account_ID = account, Employee_Type = EmployeeType)

def MemberSerializer(Email, Username, Password, Dob, Cnic, Address, PhoneNo):
    #instance.set_password(password)
    #use this to convert password
    account = AccountDB.objects.create(email = Email, username = Username, password = Password, DateOfBirth = Dob , CNIC = Cnic, Address = Address, Phone_No = PhoneNo)
    account.set_password(Password)
    account.save()
    return MemberDB.objects.create(Account_ID = account)

def MembershipSerializer(member, accountID):
    
    employee = EmployeeDB.objects.get(Account_ID = accountID)
    MembershipDB.objects.create(Member_ID = member, Approved_By = employee)

def BillSerializer(membership, amount, type):

    BillDB.objects.create(Membership_ID = membership, Bill_Amount = amount, Bill_Type = type)

def VehicleSerializer(Member, vehicleID, vehicleModel):

    vehicle = VehicleDB.objects.create(Vehicle_ID = vehicleID, Member_ID = Member, Vehicle_Model = vehicleModel)
    return vehicle

def GetMemberObject(memberID):

    return MemberDB.objects.get(Member_ID = memberID)

def getVehicleObject(vehicleID):

    return VehicleDB.objects.get(Vehicle_ID = vehicleID)

def DeleteAccountObject(accountId):
    
    account = AccountDB.objects.get(id = accountId)
    account.delete()

def DeleteMemberObject(member):

    accountIdObj = member._meta.get_field('Account_ID')
    accountId = accountIdObj.value_from_object(member)
    DeleteAccountObject(accountId)

    member.delete()

def DeleteMembershipObject(membership):

    membership.delete()

def getActiveMembershipObject(member):

    memberships = member.membership_set.all()

    for one in memberships:

        validToObj = one._meta.get_field('Valid_To')
        validTo = validToObj.value_from_object(one)

        #NON EXPIRED MEMBERSHIP
        if timezone.now() < validTo:
            return one

    #NO ACTIVE MEMBERSHIP
    return None

def getAllMembershipObjects(member):

    return member.membership_set.all()

def getBillsAmount(membership):

    bills = membership.bill_set.all()

    totalAmount = 0

    for one in bills:

        amountObj = one._meta.get_field('Bill_Amount')
        amount = amountObj.value_from_object(one)

        totalAmount += int(amount)

    return totalAmount

def getEmployeeType(accountId):

    empType = EmployeeDB.objects.filter(Account_ID = accountId).values('Employee_Type')
    return empType

def getAccountName(accountId):

    name = AccountDB.objects.filter(id = accountId).values('username')
    return name

def GetMemberDetails(memberId):

    accountId = MemberDB.objects.filter(Member_ID = memberId).values('Account_ID')
    accountId = accountId[0]['Account_ID']
    
    memberDetails = []

    username = AccountDB.objects.filter(id = accountId).values_list('username')
    email = AccountDB.objects.filter(id = accountId).values('email')
    DateOfBirth = AccountDB.objects.filter(id = accountId).values('DateOfBirth')
    CNIC = AccountDB.objects.filter(id = accountId).values('CNIC')
    Address = AccountDB.objects.filter(id = accountId).values('Address')
    Phone_No = AccountDB.objects.filter(id = accountId).values('Phone_No')
    
    memberDetails.append({'username':username[0][0]})
    memberDetails.append({'email':email[0]['email']})
    memberDetails.append({'DateOfBirth':DateOfBirth[0]['DateOfBirth']})
    memberDetails.append({'CNIC':CNIC[0]['CNIC']})
    memberDetails.append({'Address':Address[0]['Address']})
    memberDetails.append({'Phone_No':Phone_No[0]['Phone_No']})

    return memberDetails