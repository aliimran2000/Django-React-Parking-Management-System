from .Membership import Membership

from ..modelManager import DeleteMembershipObject, getActiveMembershipObject, getAllMembershipObjects

class MembershipManager:

    def __init__(self):
        self.BillingMan = None

    def initializeManagers(self, BillingMan):
        self.BillingMan = BillingMan

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
            for one in MemX:
                DeleteMembershipObject(one)

    def getActiveMembershipDues(self, M1):

        Mem1 = self.getActiveMembership(M1)

        #NO ACTIVE MEMBERSHIP, HENCE NO REMAINING DUES
        if Mem1 is None:
            return 0
        else:
            return self.BillingMan.getRemainingDues(Mem1)