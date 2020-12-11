from ..serializers import MembershipSerializer

from .BillingManager import GenerateMembershipRegistrationBill

class Membership:

    def __init__(self, member):
        self.Mem1 = MembershipSerializer(member)
        GenerateMembershipRegistrationBill(self.Mem1)