from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Bill import Bill

def GenerateMembershipRegistrationBill(membership):

    #1000Rs is MembershipGeneration Fee
    B1 = Bill(membership, 1000)