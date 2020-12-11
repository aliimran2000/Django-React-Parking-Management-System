from ..serializers import MemberSerializer
from .MembershipManager import InitiateMembership

class Member:

    #Create Function
    def __init__(self, email, username, password, DateOfBirth, CNIC, Address, Phone_No):
        self.M1 = MemberSerializer(email, username, password, DateOfBirth, CNIC, Address, Phone_No)
        InitiateMembership(self.M1)