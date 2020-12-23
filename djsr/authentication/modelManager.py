from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Employee as EmployeeDB
from .models import Accounts as AccountDB
from .models import Member as MemberDB
from .models import Membership as MembershipDB
from .models import Bill as BillDB
from .models import Vehicle as VehicleDB
from .models import Parking as ParkingDB
from .models import Slot as SlotDB

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

def ParkingSerializer(vehicle, slot):

    ParkingDB.objects.create(Vehicle_ID = vehicle, Slot_Given = slot)

def getFreeSlot():

    slots = SlotDB.objects.filter(Occupied_Status = False)

    try:
        slot = slots[0]
        slot.Occupied_Status = True
        slot.save()

        return slot
    except:
        return None

def getSlotIdBySlot(S1):

    slotIdObj = S1._meta.get_field('Slot_ID')
    slotId = slotIdObj.value_from_object(S1)

    return slotId

def markParkingExitTime(V1):

    P1 = ParkingDB.objects.get(Vehicle_ID = V1, Out_Time = None)

    currentTime = timezone.now()

    P1.Out_Time = currentTime
    P1.save()

    parkedTimeObj = P1._meta.get_field('In_Time')
    parkedTime = parkedTimeObj.value_from_object(P1)

    duration = currentTime - parkedTime
    duration_in_s = duration.total_seconds()

    #Seconds in an hour = 3600
    hoursParked = divmod(duration_in_s, 3600)[0] 

    return P1, hoursParked

def freeOccupiedSlot(V1):

    P1, hoursParked = markParkingExitTime(V1)

    slotObj = P1._meta.get_field('Slot_Given')
    slotId = slotObj.value_from_object(P1)

    S1 = SlotDB.objects.get(Slot_ID = slotId)
    S1.Occupied_Status = False
    S1.save()

    return hoursParked

def GetMemberObject(memberID):

    return MemberDB.objects.get(Member_ID = memberID)

def getVehicleObject(vehicleID):

    return VehicleDB.objects.get(Vehicle_ID = vehicleID)

def validateVehicleByMember(M1, vehicleId):

    memberIdObj = M1._meta.get_field('Member_ID')
    memberId = memberIdObj.value_from_object(M1)

    vehicle = VehicleDB.objects.get(Member_ID = memberId)

    vehicleIdObj = vehicle._meta.get_field('Vehicle_ID')
    vehicleId2 = vehicleIdObj.value_from_object(vehicle)

    if vehicleId == vehicleId2:
        return vehicle
    else:
        return None

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

def DeleteVehicleObject(vehicle):

    vehicle.delete()

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

def getOverdueBills(Mem1):

    bills = Mem1.bill_set.all()

    totalAmount = 0

    for one in bills:

        dueDateObj = one._meta.get_field('Due_Date')
        dueDate = dueDateObj.value_from_object(one)

        if (timezone.now() > dueDate) :

            amountObj = one._meta.get_field('Bill_Amount')
            amount = amountObj.value_from_object(one)

            totalAmount += int(amount)

    return totalAmount

def getAccountType(accountId):

    #FIRST CHECK IF THE ACCOUNT IS EMPLOYEE
    try:
        emp = EmployeeDB.objects.filter(Account_ID = accountId).values('Employee_Type')
        return emp[0]['Employee_Type']
    except:
        return "M"

def getAccountName(accountId):

    name = AccountDB.objects.filter(id = accountId).values('username')
    return name[0]

def GetMemberDetails(memberId):

    accountId = MemberDB.objects.filter(Member_ID = memberId).values('Account_ID')
    
    dict = {}
    
    try:
    
        accountId = accountId[0]['Account_ID']
        username = AccountDB.objects.filter(id = accountId).values_list('username')
        email = AccountDB.objects.filter(id = accountId).values('email')
        DateOfBirth = AccountDB.objects.filter(id = accountId).values('DateOfBirth')
        CNIC = AccountDB.objects.filter(id = accountId).values('CNIC')
        Address = AccountDB.objects.filter(id = accountId).values('Address')
        Phone_No = AccountDB.objects.filter(id = accountId).values('Phone_No')
        
        dict['username'] = username[0][0]
        dict['email'] = email[0]['email']
        dict['DateOfBirth'] = DateOfBirth[0]['DateOfBirth']
        dict['CNIC'] = CNIC[0]['CNIC']
        dict['Address']= Address[0]['Address']
        dict['Phone_No']=Phone_No[0]['Phone_No']
    
    except Exception as E:
    
        print(E)
        dict['username'] = 'NOT FOUND'
    
    return dict

def isMemberCredentialValid(userName, password):

    try:
        account = AccountDB.objects.get(username = userName)
    except:
        #INVALID USERNAME
        return None

    if (account.check_password(password) == True):

        accountIdObj = account._meta.get_field('id')
        accountId = accountIdObj.value_from_object(account)

        memberId = MemberDB.objects.filter(Account_ID = accountId).values_list('Member_ID')

        return memberId[0][0]

    else:
        return None