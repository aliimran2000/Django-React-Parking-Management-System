from .Parking import Parking
from ..modelManager import getFreeSlot, getSlotIdBySlot, freeOccupiedSlotAndGetTime, getAllParkingObjects, deleteParkingObject, isAlreadyParked

class ParkingLotManager:

    def __init__(self):

        self.MemberMan = None
        self.BillingMan = None
        self.VehicleMan = None
        self.MembershipMan = None
        self.EmployeeMan = None

    def initializeManagers(self, memberMan, billingMan, vehicleMan, membershipMan, employeeMan):

        self.MemberMan = memberMan
        self.BillingMan = billingMan
        self.VehicleMan = vehicleMan
        self.MembershipMan = membershipMan
        self.EmployeeMan = employeeMan

    def getFreeSlot(self):
        return getFreeSlot()

    def freeOccupiedSlotAndGetTime(self, V1):
        return freeOccupiedSlotAndGetTime(V1)

    def checkAlreadyParkedStatus(self, V1):
        return isAlreadyParked(V1)

    def parkVehicle(self, memberId, vehicleId, employeeId):

        M1 = self.MemberMan.getMemberById(memberId)

        Mem1 = self.MembershipMan.getActiveMembership(M1)

        if Mem1 is None:
            return "EXPIRED"

        dues = self.BillingMan.checkOverdueBills(Mem1)

        if dues > 0 :
            return "UNCLEARED DUES"

        V1 = self.VehicleMan.validateVehicle(M1, vehicleId)

        if V1 is None:
            return "NOT REGISTERED"

        status = self.checkAlreadyParkedStatus(V1)
        if status == True:
            return "ALREADY PARKED"

        S1 = self.getFreeSlot()

        if S1 == None:
            return "PARKING FULL"

        E1 = self.EmployeeMan.getEmployeeById(employeeId)

        P1 = Parking(V1, S1, E1)

        return getSlotIdBySlot(S1)

    def exitVehicle(self, memberId, vehicleId):

        M1 = self.MemberMan.getMemberById(memberId)
        Mem1 = self.MembershipMan.getActiveMembership(M1)

        if Mem1 is None:
            return "EXPIRED MEMBERSHIP"

        V1 = self.VehicleMan.validateVehicle(M1, vehicleId)

        if V1 is None:
            return "NOT REGISTERED"

        hoursParked = self.freeOccupiedSlotAndGetTime(V1)

        return self.BillingMan.generateParkingFee(Mem1, hoursParked)

    def getAllParkings(self, V1):

        getAllParkingObjects(V1)

    def removeAllParkings(self, V1):

        PKX = self.getAllParkings(V1)

        if PKX is not None:
    
            for PK1 in PKX:

                deleteParkingObject(PK1)