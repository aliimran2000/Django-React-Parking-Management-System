from .Bill import Bill

from ..modelManager import getBillsAmount, getOverdueBills

class BillingManager:

    def __init__(self):
        self.__membershipRegistration = 1000
        self.__vehicleRegistration = 500
        self.__membershipRenewal = 800

    def GenerateMembershipRegistrationBill(self, membership):

        B1 = Bill(membership, self.__membershipRegistration, 'MC')

    def getRemainingDues(self, membership):

        return getBillsAmount(membership)

    def generateVehicleRegistrationBill(self, membership):

        B1 = Bill(membership, self.__vehicleRegistration, 'VR')

    def generateMembershipRenewalBill(self, membership):

        B1 = Bill(membership, self.__membershipRenewal, 'MR')

    def checkOverdueBills(self, Mem1):

        return getOverdueBills(Mem1)