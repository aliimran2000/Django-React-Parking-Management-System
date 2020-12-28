from .Membership import Membership

from ..modelManager import DeleteMembershipObject, getActiveMembershipObject, getAllMembershipObjects

class MembershipManager:

    def __init__(self):
        self.BillingMan = None
        self.MemberMan = None
        self.EmployeeMan = None
        
    def initializeManagers(self, BillingMan, MemberMan, EmployeeMan):
        self.BillingMan = BillingMan
        self.MemberMan = MemberMan
        self.EmployeeMan = EmployeeMan

    def getActiveMembership(self, member):
        
        return getActiveMembershipObject(member, False)

    def getLastActiveMembership(self, member):

        return getActiveMembershipObject(member, True)

    def InitiateMembership(self, M1, E1):

        Membership(M1, E1)
        
        Mem1 = self.getActiveMembership(M1)

        self.BillingMan.GenerateMembershipRegistrationBill(Mem1)
    
    def getAllMemberships(self, member):

        return getAllMembershipObjects(member)

    def removeMembership(self, M1):

        MemX = self.getAllMemberships(M1)

        if MemX is not None:

            for Mem1 in MemX:

                self.BillingMan.removeMembershipBills(Mem1)
                DeleteMembershipObject(Mem1)

    def getActiveMembershipDues(self, M1):

        Mem1 = self.getActiveMembership(M1)

        #NO ACTIVE MEMBERSHIP, HENCE NO REMAINING DUES
        if Mem1 is None:
            return 0
        else:
            return self.BillingMan.getRemainingDues(Mem1)

    def isActiveMembershipExpired(self, M1):

        Mem1 = self.getActiveMembership(M1)
        
        if Mem1 is None:
            return True
        else:
            return False

    def renewMembership(self, memberId, employeeId):

        M1 = self.MemberMan.getMemberById(memberId)

        if (self.isActiveMembershipExpired(M1) == False):
            return "Not Expired"
        
        MemT = self.getLastActiveMembership(M1)
        dues = self.BillingMan.getRemainingDues(MemT)

        if dues > 0 :
            return "Uncleared Dues"

        E1 = self.EmployeeMan.getEmployeeById(employeeId)

        Membership(M1, E1)
        
        Mem1 = self.getActiveMembership(M1)

        self.BillingMan.generateMembershipRenewalBill(Mem1)

        return "OK"