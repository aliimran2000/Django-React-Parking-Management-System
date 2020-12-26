from .Member import Member

from ..modelManager import GetMemberObject, DeleteMemberObject, GetMemberDetails

class MemberManager:

    def __init__(self):
        self.MembershipMan = None
        self.VehicleMan = None
        self.EmployeeMan = None

    def initializeManagers(self, MembershipMan, VehicleMan, EmployeeMan):
        self.MembershipMan = MembershipMan
        self.VehicleMan = VehicleMan
        self.EmployeeMan = EmployeeMan

    def registerMember(self, email, username, password, DateOfBirth, Cnic, Address, Phone_No, Approved_By):

        E1 = self.EmployeeMan.getEmployeeById(Approved_By)

        member = Member(email, username, password, DateOfBirth, Cnic, Address, Phone_No, E1)
        M1 = self.getMemberById(member.getMemberId())

        self.MembershipMan.InitiateMembership(M1, E1)

    def deregisterMember(self, memberId):
        
        M1 = GetMemberObject(memberId)

        remainingDues = self.MembershipMan.getActiveMembershipDues(M1)

        if remainingDues > 0 :
            return "Fail"

        else:
            self.MembershipMan.removeMembership(M1)
            self.VehicleMan.removeAllVehicles(M1)
            DeleteMemberObject(M1)
            return "OK"          

    def getMemberById(self, memberId):
        
        return GetMemberObject(memberId)

    def getMemberDetails(self, memberId):

        memberDetails = GetMemberDetails(memberId)
        return memberDetails