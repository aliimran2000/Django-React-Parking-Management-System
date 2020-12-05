from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)
 


class Employee_Type(models.Model):
    Emp_Type_ID = models.AutoField(primary_key=True) 
    Emp_Type = models.CharField(max_length=55,blank=False,null=False)


class Employee(models.Model):
    Emp_ID = models.AutoField(primary_key=True)
    Employee_Type = models.ForeignKey(Employee_Type, on_delete=models.CASCADE)
    


class Membership(models.Model):
    Membership_ID = models.AutoField(primary_key=True)




class Member(AbstractUser):
    member_id = models.AutoField(primary_key=True)   
    