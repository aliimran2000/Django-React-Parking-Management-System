from datetime import datetime
from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils import timezone

class Accounts(User):
    DateOfBirth = models.DateField(blank=False, null=False)
    CNIC = models.CharField(max_length=13, blank=False, null=False)
    Address = models.CharField(max_length=100, blank=False, null=False)
    Phone_No = models.CharField(max_length=11, blank=False, null=False)


class Employee(models.Model):
    Employee_ID = models.AutoField(primary_key=True)
    Account_ID = models.ForeignKey(Accounts,on_delete=CASCADE, blank=False, null=False)

class Membership(models.Model):
    Membership_ID = models.AutoField(primary_key=True)
    Approved_By = models.ForeignKey(
    Employee, on_delete=CASCADE, blank=False, null=False)
    Valid_From = models.DateTimeField(default=timezone.now)
    Valid_To = models.DateTimeField(datetime, blank=False, null=False)

class Member(models.Model):
    Member_ID = models.AutoField(primary_key=True)
    Account_ID = models.ForeignKey(Accounts,on_delete=CASCADE, blank=False, null=False)
    Member_ID = models.ForeignKey(
    Membership, on_delete=CASCADE, blank=False, null=False)


