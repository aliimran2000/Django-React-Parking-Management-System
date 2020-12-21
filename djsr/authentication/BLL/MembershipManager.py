from datetime import datetime, timezone
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Membership import Membership

from ..serializers import DeleteMembershipObject, getActiveMembershipObject, getAllMembershipObjects

class MembershipManager:

    def __init__(self):
        self.__membershipInitiationFee = 1000
        self.BillingMan = None

    def initializeManagers(self, BillingMan):
        self.BillingMan = BillingMan

    def InitiateMembership(self, member):

        Mem1 = Membership(member, self.__membershipInitiationFee, self.BillingMan)

    def getActiveMembership(self, member):
        
        return getActiveMembershipObject(member)

    def getAllMemberships(self, member):

        return getAllMembershipObjects(member)

    def removeMembership(self, M1):

        Mem1 = self.getAllMemberships(M1)

        if Mem1 is not None:
            for one in Mem1:
                DeleteMembershipObject(one)

    def getActiveMembershipDues(self, M1):

        Mem1 = self.getActiveMembership(M1)

        #NO ACTIVE MEMBERSHIP, HENCE NO REMAINING DUES
        if Mem1 is None:
            return 0
        else:
            return self.BillingMan.getRemainingDues(Mem1)