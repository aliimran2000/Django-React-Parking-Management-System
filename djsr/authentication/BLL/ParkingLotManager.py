from .Parking import Parking
from ..modelManager import getFreeSlot, getSlotIdBySlot, freeOccupiedSlot

class ParkingLotManager:

    def __init__(self):

        self.MemberMan = None
        self.BillingMan = None
        self.VehicleMan = None

    def initializeManagers(self, memberMan, billingMan, vehicleMan):

        self.MemberMan = memberMan
        self.BillingMan = billingMan
        self.VehicleMan = vehicleMan

    def getFreeSlot(self):
        return getFreeSlot()

    def freeOccupiedSlot(self, V1):
        return freeOccupiedSlot(V1)

    def parkVehicle(self, memberId, vehicleId):

        M1, Mem1 = self.MemberMan.getMemberAndMembership(memberId)

        if Mem1 is None:
            return "EXPIRED"

        dues = self.BillingMan.checkOverdueBills(Mem1)

        if dues > 0 :
            return "UNCLEARED DUES"

        V1 = self.VehicleMan.validateVehicle(M1, vehicleId)

        if V1 is None:
            return "NOT REGISTERED"

        S1 = self.getFreeSlot()

        if S1 == None:
            return "PARKING FULL"

        P1 = Parking(V1, S1)

        return getSlotIdBySlot(S1)

    def exitVehicle(self, memberId, vehicleId):

        M1, Mem1 = self.MemberMan.getMemberAndMembership(memberId)

        V1 = self.VehicleMan.validateVehicle(M1, vehicleId)

        if V1 is None:
            return "NOT REGISTERED"

        hoursParked = self.freeOccupiedSlot(V1)

        return self.BillingMan.generateParkingFee(Mem1, hoursParked)