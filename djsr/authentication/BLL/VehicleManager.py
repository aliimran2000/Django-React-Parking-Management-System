from .Vehicle import Vehicle

from ..modelManager import getVehicleObject, DeleteVehicleObject, validateVehicleByMember, getVehiclesDetail, getVehicleObjects, DeleteVehicleObject

class VehicleManager:

    def __init__(self):
        self.BillingMan = None
        self.MemberMan = None
        self.ParkingLotMan = None
        self.MembershipMan = None
        self.EmployeeMan = None

    def initializeManagers(self, BillingMan, MemberMan, ParkingLotMan, MembershipMan, EmployeeMan):
        self.BillingMan = BillingMan
        self.MemberMan = MemberMan
        self.ParkingLotMan = ParkingLotMan
        self.MembershipMan = MembershipMan
        self.EmployeeMan = EmployeeMan
    
    def validateVehicle(self, M1, vehicleId):

        return validateVehicleByMember(M1, vehicleId)

    def registerVehicle(self, memberId, vehicleId, vehicleModel, employeeId):
        
        M1 = self.MemberMan.getMemberById(memberId)
        Mem1 = self.MembershipMan.getActiveMembership(M1)

        if Mem1 is None:
            return "MEMBERSHIP EXPIRED"

        E1 = self.EmployeeMan.getEmployeeById(employeeId)

        Vehicle(M1, E1, vehicleId, vehicleModel)
        V1 = getVehicleObject(vehicleId)

        self.BillingMan.generateVehicleRegistrationBill(Mem1)
    
        return "OK"

    def deregisterVehicle(self, memberId, vehicleId):

        M1 = self.MemberMan.getMemberById(memberId)
        V1 = self.validateVehicle(M1, vehicleId)

        if V1 is None:
            return "401"

        DeleteVehicleObject(V1)

        return "OK"

    def getVehiclesDetail(self, memberId):

        return getVehiclesDetail(memberId)

    def getAllVehicles(self, M1):

        return getVehicleObjects(M1)

    def removeAllVehicles(self, M1):

        VX = self.getAllVehicles(M1)

        if VX is not None:

            for V1 in VX:
                
                self.ParkingLotMan.removeAllParkings(V1)
                DeleteVehicleObject(V1)