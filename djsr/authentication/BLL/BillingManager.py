from .Bill import Bill

from ..modelManager import getBillsAmount

class BillingManager:

    def GenerateMembershipRegistrationBill(self, membership, fee):

        B1 = Bill(membership, fee)

    def getRemainingDues(self, membership):

        return getBillsAmount(membership)