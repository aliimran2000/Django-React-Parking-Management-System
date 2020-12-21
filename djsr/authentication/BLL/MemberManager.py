from .Member import Member

from ..modelManager import GetMemberObject, DeleteMemberObject

class MemberManager:

    def __init__(self):
        self.MembershipMan = None

    def initializeManagers(self, MembershipMan):
        self.MembershipMan = MembershipMan

    def registerMember(self, email, username, password, DateOfBirth, Cnic, Address, Phone_No, Approved_By):

        Member(email, username, password, DateOfBirth, Cnic, Address, Phone_No, self.MembershipMan, Approved_By)

    def deregisterMember(self, memberId):
        
        M1 = GetMemberObject(memberId)

        remainingDues = self.MembershipMan.getActiveMembershipDues(M1)

        if remainingDues > 0 :
            return "Fail"

        else:
            self.MembershipMan.removeMembership(M1)
            DeleteMemberObject(M1)
            return "OK"          

    def getMemberById(self, memberId):
        return GetMemberObject(memberId)