from ..modelManager import PaymentSerializer

class Payment:

    def __init__(self, bill, paymentMethod, employee):

        #CREATE FUNCTION
        PaymentSerializer(bill, paymentMethod, employee)