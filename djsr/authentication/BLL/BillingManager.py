from .Bill import Bill

from ..modelManager import getBillsAmount, getOverdueBills, getBillsDetail, getAllBillObjects, getBillObjectById, deleteBillObject, changePaidStatus

class BillingManager:

    def __init__(self):
        self.__membershipRegistration = 1000
        self.__vehicleRegistration = 500
        self.__membershipRenewal = 800
        self.__parkPerHour = 100
        
        self.MemberMan = None
        self.MembershipMan = None
        self.PaymentMan = None
        self.EmployeeMan = None

    def initializeManagers(self, MemberMan, MembershipMan, PaymentMan, EmployeeMan):
        self.MemberMan = MemberMan
        self.MembershipMan = MembershipMan
        self.PaymentMan = PaymentMan
        self.EmployeeMan = EmployeeMan

    def GenerateMembershipRegistrationBill(self, membership):

        B1 = Bill(membership, self.__membershipRegistration, 'MC')

    def getRemainingDues(self, membership):

        return getBillsAmount(membership)

    def generateVehicleRegistrationBill(self, membership):

        B1 = Bill(membership, self.__vehicleRegistration, 'VR')

    def generateMembershipRenewalBill(self, membership):

        B1 = Bill(membership, self.__membershipRenewal, 'MR')

    def generateParkingFee(self, Mem1, hoursParked):

        if hoursParked < 1:
            hoursParked = 1

        totalParkFee = self.__parkPerHour * hoursParked
        B1 = Bill(Mem1, int(totalParkFee), 'PV')
        return int(totalParkFee)

    def checkOverdueBills(self, Mem1):

        return getOverdueBills(Mem1)

    def getBillsDetail(self, memberId):

        M1 = self.MemberMan.getMemberById(memberId)
        Mems = self.MembershipMan.getAllMemberships(M1)

        return getBillsDetail(Mems, False)

    def getAllUnpaidBills(self, Mem1):

        return getBillsDetail(Mem1, True)

    def getUnpaidBillsDetail(self, memberId):

        M1 = self.MemberMan.getMemberById(memberId)
        Mem1 = self.MembershipMan.getActiveMembership(M1)
        return self.getAllUnpaidBills(Mem1)

    def getAllBills(self, Mem1):
        
        return getAllBillObjects(Mem1)

    def removeMembershipBills(self, Mem1):

        BX = self.getAllBills(Mem1)

        if BX is not None:

            for B1 in BX:
                self.PaymentMan.removeBillsPayment(B1)
                deleteBillObject(B1)

    def getBillById(self, id):

        return getBillObjectById(id)

    def markBillAsPaid(self, B1):

        changePaidStatus(B1)

    def payBill(self, billIds, paymentMethod, supervisorId):

        E1 = self.EmployeeMan.getEmployeeById(supervisorId)

        for one in billIds:

            B1 = self.getBillById(one)

            self.PaymentMan.generatePayment(B1, paymentMethod, E1)
            self.markBillAsPaid(B1)