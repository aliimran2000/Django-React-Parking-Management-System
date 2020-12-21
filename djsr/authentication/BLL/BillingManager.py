from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Bill import Bill

from ..serializers import getBillsAmount

class BillingManager:

    def GenerateMembershipRegistrationBill(self, membership, fee):

        B1 = Bill(membership, fee)

    def getRemainingDues(self, membership):

        return getBillsAmount(membership)