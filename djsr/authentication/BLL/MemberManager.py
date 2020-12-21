from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Member import Member

from ..serializers import GetMemberObject, DeleteMemberObject

from .MembershipManager import MembershipManager
#removeMembership, getActiveMembershipDues

class MemberManager:

    def __init__(self):
        self.MembershipMan = None

    def initializeManagers(self, MembershipMan):
        self.MembershipMan = MembershipMan

    def registerMember(self):

        MembershipMan = self.MembershipMan
        
        class registerMemberApiView(APIView):

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
                        
                Member(email, username, password, DateOfBirth, Cnic, Address, Phone_No, MembershipMan)
                return Response("Member Request for Registration is Parked For Approval", status=status.HTTP_201_CREATED)

        return registerMemberApiView.as_view()

    def deregisterMember(self):

        MembershipMan = self.MembershipMan

        class deregisterMemberApiView(APIView):

            #IMPLEMENT DEREGISTER MEMBER VIEW IN FRONTEND OF ADMIN
            permission_classes = (permissions.AllowAny,)
            
            def post(self, request, format='json'):

                memberId = request.data['Member_ID']
                M1 = GetMemberObject(memberId)

                remainingDues = MembershipMan.getActiveMembershipDues(M1)

                if remainingDues > 0 :
                    return Response("Member "+ memberId +" has uncleared dues. Unable to deregister member", status=status.HTTP_400_BAD_REQUEST)

                else:
                    MembershipMan.removeMembership(M1)
                    DeleteMemberObject(M1)
                    return Response("Member "+ memberId +" Has Successfully Been deregistered", status=status.HTTP_201_CREATED)

        return deregisterMemberApiView.as_view()

    def getMemberById(self, memberId):
        return GetMemberObject(memberId)