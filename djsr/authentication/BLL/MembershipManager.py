from .Membership import Membership

from ..modelManager import DeleteMembershipObject, getActiveMembershipObject, getAllMembershipObjects

class MembershipManager:

    def __init__(self):
        self.BillingMan = None
        self.MemberMan = None

    def initializeManagers(self, BillingMan, MemberMan):
        self.BillingMan = BillingMan
        self.MemberMan = MemberMan

    def getActiveMembership(self, member):
        
        return getActiveMembershipObject(member)

    def InitiateMembership(self, member, Approved_By):

        Membership(member, Approved_By)
        
        Mem1 = self.getActiveMembership(member)

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

    def renewMembership(self, memberId, approvedBy):

        M1 = self.MemberMan.getMemberById(memberId)

        if (self.isActiveMembershipExpired(M1) == False):
            return "Not Expired"
        
        Membership(M1, approvedBy)
        
        Mem1 = self.getActiveMembership(M1)

        self.BillingMan.generateMembershipRenewalBill(Mem1)

        return "OK"