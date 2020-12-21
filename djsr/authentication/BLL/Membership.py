from ..modelManager import MembershipSerializer

class Membership:

    def __init__(self, member, Approved_By):
        MembershipSerializer(member, Approved_By)