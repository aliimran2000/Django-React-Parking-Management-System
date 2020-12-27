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

    def getMemberById(self, memberId):
        
        return GetMemberObject(memberId, False)

    def getMemberByAccountId(self, accountId):

        return GetMemberObject(accountId, True)

    def registerMember(self, email, username, password, dateOfBirth, cnic, address, phoneNo, employeeId):

        E1 = self.EmployeeMan.getEmployeeById(employeeId)

        member = Member(email, username, password, dateOfBirth, cnic, address, phoneNo, E1)
        M1 = self.getMemberById(member.getMemberId())

        self.MembershipMan.InitiateMembership(M1, E1)

        return "OK"

    def deregisterMember(self, memberId):
        
        M1 = self.getMemberById(memberId)

        remainingDues = self.MembershipMan.getActiveMembershipDues(M1)

        if remainingDues > 0 :
            return "Fail"

        else:
            self.MembershipMan.removeMembership(M1)
            self.VehicleMan.removeAllVehicles(M1)
            DeleteMemberObject(M1)
            return "OK"          

    def getMemberDetails(self, memberId):

        memberDetails = GetMemberDetails(memberId)
        return memberDetails