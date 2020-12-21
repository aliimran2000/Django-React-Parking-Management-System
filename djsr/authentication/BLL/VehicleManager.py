from .Vehicle import Vehicle

from ..modelManager import getVehicleObject

class VehicleManager:

    def __init__(self):
        self.BillingMan = None

    def initializeManagers(self, BillingMan):
        self.BillingMan = BillingMan

    def registerVehicle(self, M1, Mem1, Vehicle_ID, Vehicle_Model):
        
        Vehicle(M1, Vehicle_ID, Vehicle_Model)

        V1 = getVehicleObject(Vehicle_ID)
        self.BillingMan.generateVehicleRegistrationBill(Mem1)