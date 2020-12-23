from .Member import Member

from ..modelManager import GetMemberObject, DeleteMemberObject, GetMemberDetails

class MemberManager:

    def __init__(self):
        self.MembershipMan = None

    def initializeManagers(self, MembershipMan, VehicleMan):
        self.MembershipMan = MembershipMan
        self.VehicleMan = VehicleMan

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

    def registerVehicle(self, Vehicle_ID, Member_ID, Vehicle_Model):

        M1 = self.getMemberById(Member_ID)
        Mem1 = self.MembershipMan.getActiveMembership(M1)
        self.VehicleMan.registerVehicle(M1, Mem1, Vehicle_ID, Vehicle_Model)

    def getMemberDetails(self, memberId):

        memberDetails = GetMemberDetails(memberId)
        return memberDetails

    def renewMembership(self, memberId, approvedBy):

        M1 = self.getMemberById(memberId)

        if (self.MembershipMan.isActiveMembershipExpired(M1) == False):
            return "Not Expired"
        
        self.MembershipMan.renewMembership(M1, approvedBy)

        return "OK"

    def getMemberAndMembership(self, memberId):

        M1 = self.getMemberById(memberId)
        Mem1 = self.MembershipMan.getActiveMembership(M1)
        return M1, Mem1