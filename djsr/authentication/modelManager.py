from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Employee as EmployeeDB
from .models import Accounts as AccountDB
from .models import Member as MemberDB
from .models import Membership as MembershipDB
from .models import Bill as BillDB

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
    return MembershipDB.objects.create(Member_ID = member, Approved_By = employee)

def BillSerializer(membership, amount):

    BillDB.objects.create(Membership_ID = membership, Bill_Amount = amount)

def GetMemberObject(memberID):

    return MemberDB.objects.get(Member_ID = memberID)

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