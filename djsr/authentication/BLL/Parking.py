from ..modelManager import ParkingSerializer

class Parking:

    def __init__(self, vehicle, slot):
        ParkingSerializer(vehicle, slot)