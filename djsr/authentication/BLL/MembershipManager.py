from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from .Membership import Membership

def InitiateMembership(member):

    Mem1 = Membership(member)