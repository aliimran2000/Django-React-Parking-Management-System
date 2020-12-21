from ..modelManager import MemberSerializer

class Member:

    #Create Function
    def __init__(self, email, username, password, DateOfBirth, CNIC, Address, Phone_No, MembershipMan, Approved_By):
        self.M1 = MemberSerializer(email, username, password, DateOfBirth, CNIC, Address, Phone_No)
        MembershipMan.InitiateMembership(self.M1, Approved_By)