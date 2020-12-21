from ..modelManager import MembershipSerializer

class Membership:

    def __init__(self, member, fee, BillMan, Approved_By):
        self.BillMan = BillMan
        self.Mem1 = MembershipSerializer(member, Approved_By)
        self.BillMan.GenerateMembershipRegistrationBill(self.Mem1, fee)