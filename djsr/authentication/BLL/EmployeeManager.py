from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Employee import Employee

class Register_Employee(APIView):

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

        Employee(email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type)
        return Response("Employee of Type " + Employee_Type + " has successfully been registered", status=status.HTTP_201_CREATED)
