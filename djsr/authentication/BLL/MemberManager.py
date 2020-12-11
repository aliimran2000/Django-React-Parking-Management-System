from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Member import Member

class Register_Member_Request(APIView):

    #IMPLEMENT REGISTER MEMBER VIEW IN FRONTEND OF ADMIN
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):

        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        DateOfBirth = request.data['DateOfBirth']
        Cnic = request.data['CNIC']
        Address = request.data['Address']
        Phone_No = request.data['Phone_No']

        Member(email, username, password, DateOfBirth, Cnic, Address, Phone_No)
        return Response("Member Request for Registration is Parked For Approval", status=status.HTTP_201_CREATED)
