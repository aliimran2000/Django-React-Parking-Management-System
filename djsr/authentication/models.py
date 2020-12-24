from datetime import datetime
from django.contrib.auth.models import Group , AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils import timezone

class Accounts(AbstractUser):

    DateOfBirth = models.DateField(default='2000-01-01',blank=True, null=True)
    CNIC = models.CharField(max_length=13, blank=False, null=False, unique=True)
    Address = models.CharField(max_length=100, blank=False, null=False)
    Phone_No = models.CharField(max_length=11, blank=False, null=False, unique=True)
    

class Employee(models.Model):
    
    Employee_ID = models.AutoField(primary_key=True)
    Account_ID = models.OneToOneField(Accounts,on_delete=CASCADE, blank=False, null=False)
    
    Employee_Type_List = [
        ('PE','ParkingEmployee'),
        ('PA','ParkingAdmin'),
    ]
    
    Employee_Type = models.CharField(
        max_length=2,
        choices=Employee_Type_List,
        default='ParkingEmployee',
    )    

#MEMBER HAS 1-* Relation with Membership (membership is expired but not deleted)
class Member(models.Model):

    Member_ID = models.AutoField(primary_key=True)
    Account_ID = models.OneToOneField(Accounts,on_delete=CASCADE, blank=False, null=False)

class Membership(models.Model):

    Membership_ID = models.AutoField(primary_key=True)
    Member_ID = models.ForeignKey(Member, on_delete=CASCADE, blank=False, null=False)
    Approved_By = models.ForeignKey(Employee, on_delete=CASCADE, blank=False, null=False)
    Valid_From = models.DateTimeField(default=timezone.now)
    Valid_To = models.DateTimeField(default= (timezone.now() + timezone.timedelta(days=365)))

class Bill(models.Model):

    Bill_ID = models.AutoField(primary_key=True)
    Membership_ID = models.ForeignKey(Membership, on_delete=CASCADE, blank=False, null=False)
    Generated_Date = models.DateTimeField(default=timezone.now)
    Due_Date = models.DateTimeField(default= (timezone.now() + timezone.timedelta(weeks=4)))
    Paid_Status = models.BooleanField(default = False, blank=False, null=False)
    Bill_Amount = models.CharField(max_length=10, blank=False, null=False)

    Bill_Type_List = [
        ('MC','MemberRegistration'),
        ('VR','VehicleRegistration'),
        ('PV','ParkVehicle'),
        ('MR','MembershipRenewal'),
    ]

    Bill_Type = models.CharField(
        max_length=2,
        choices=Bill_Type_List,
        default='MemberRegistration',
    )    

class Payment(models.Model):

    Payment_ID = models.AutoField(primary_key=True)
    Bill_ID = models.OneToOneField(Bill, on_delete=CASCADE, blank=False, null=False)
    Payment_Date = models.DateTimeField(default = timezone.now())
    Payment_Supervisor = models.ForeignKey(Employee, on_delete=CASCADE, blank=False, null=False)

    Payment_Method_List = [
        ('V','Visa'),
        ('M','Mastercard'),
        ('C','Cash')
    ]

    Payment_Method = models.CharField(
        max_length=2,
        choices= Payment_Method_List,
        default='Cash',
    )

class Vehicle(models.Model):

    Vehicle_ID = models.CharField(primary_key=True, max_length=10)
    Member_ID = models.ForeignKey(Member, on_delete=CASCADE, blank=False, null=False)
    Vehicle_Model = models.CharField(max_length=50, blank=False, null=False)

class Slot(models.Model):

    Slot_ID = models.CharField(primary_key=True, max_length=10)
    Occupied_Status = models.BooleanField(default=False)

class Parking(models.Model):

    Parking_ID = models.AutoField(primary_key=True)
    Vehicle_ID = models.ForeignKey(Vehicle, on_delete=CASCADE, blank=False, null=False)
    In_Time = models.DateTimeField(default = timezone.now())
    Out_Time = models.DateTimeField(blank=True, null=True)
    Slot_Given = models.ForeignKey(Slot, on_delete=CASCADE, blank=False, null=False)