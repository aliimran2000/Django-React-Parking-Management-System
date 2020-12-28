from ..modelManager import BillSerializer

class Bill:

    #Create Function
    def __init__(self,membership, amount, type):
        BillSerializer(membership, amount, type)