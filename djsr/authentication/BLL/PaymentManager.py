from .Payment import Payment

from ..modelManager import getPaymentObject, deletePaymentObject

class PaymentManager:

    def __init__(self):

        pass

    def getPayment(self, B1):

        return getPaymentObject(B1)

    def removeBillsPayment(self, B1):

        P1 = self.getPayment(B1)
        
        if P1 is not None:

            deletePaymentObject(P1)