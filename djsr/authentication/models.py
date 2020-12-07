from datetime import datetime
from django.contrib.auth.models import User, Group , AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils import timezone

class Accounts(AbstractUser):
    DateOfBirth = models.DateField(default='2000-01-01',blank=True, null=True)
    CNIC = models.CharField(max_length=13, blank=False, null=False)
    Address = models.CharField(max_length=100, blank=False, null=False)
    Phone_No = models.CharField(max_length=11, blank=False, null=False)
    

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


class Membership(models.Model):
    Membership_ID = models.AutoField(primary_key=True)
    Approved_By = models.ForeignKey(Employee, on_delete=CASCADE, blank=False, null=False)
    Valid_From = models.DateTimeField(default=timezone.now)
    Valid_To = models.DateTimeField(default= (timezone.now() + timezone.timedelta(days=365)) )

class Member(models.Model):
    Member_ID = models.AutoField(primary_key=True)
    Account_ID = models.OneToOneField(Accounts,on_delete=CASCADE, blank=False, null=False)
    Membership_ID = models.ForeignKey(Membership, on_delete=CASCADE, blank=False, default=1)#CHANGE LATER ON DEFAULT=1
