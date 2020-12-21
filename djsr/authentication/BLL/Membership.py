from ..serializers import MembershipSerializer

class Membership:

    def __init__(self, member, fee, BillMan):
        self.BillMan = BillMan
        self.Mem1 = MembershipSerializer(member)
        self.BillMan.GenerateMembershipRegistrationBill(self.Mem1, fee)