from .Vehicle import Vehicle

from ..modelManager import getVehicleObject, DeleteVehicleObject, validateVehicleByMember

class VehicleManager:

    def __init__(self):
        self.BillingMan = None
        self.MemberMan = None

    def initializeManagers(self, BillingMan, MemberMan):
        self.BillingMan = BillingMan
        self.MemberMan = MemberMan

    def validateVehicle(self, M1, vehicleId):

        return validateVehicleByMember(M1, vehicleId)

    def registerVehicle(self, M1, Mem1, Vehicle_ID, Vehicle_Model):
        
        Vehicle(M1, Vehicle_ID, Vehicle_Model)

        V1 = getVehicleObject(Vehicle_ID)
        self.BillingMan.generateVehicleRegistrationBill(Mem1)
    
    def deregisterVehicle(self, memberId, vehicleId):

        M1 = self.MemberMan.getMemberById(memberId)
        V1 = self.validateVehicle(M1, vehicleId)

        if V1 is None:
            return "401"

        DeleteVehicleObject(V1)

        return "OK"