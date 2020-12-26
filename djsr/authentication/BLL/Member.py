from ..modelManager import MemberSerializer

class Member:

    #Create Function
    def __init__(self, email, username, password, DateOfBirth, CNIC, Address, Phone_No, E1):
        self.memberId = MemberSerializer(email, username, password, DateOfBirth, CNIC, Address, Phone_No)

    def getMemberId(self):
        return self.memberId