from datetime import datetime, timezone
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Membership import Membership

from ..serializers import DeleteMembershipObject, getActiveMembershipObject, getAllMembershipObjects

from .BillingManager import getRemainingDues

def InitiateMembership(member):

    Mem1 = Membership(member)

def getActiveMembership(member):
    
    return getActiveMembershipObject(member)

def getAllMemberships(member):

    return getAllMembershipObjects(member)

def removeMembership(M1):

    Mem1 = getAllMemberships(M1)

    if Mem1 is not None:
        for one in Mem1:
            DeleteMembershipObject(one)

def getActiveMembershipDues(M1):

    Mem1 = getActiveMembership(M1)

    #NO ACTIVE MEMBERSHIP, HENCE NO REMAINING DUES
    if Mem1 is None:
        return 0
    else:
        return getRemainingDues(Mem1)