from ..modelManager import EmployeeSerializer

class Employee:

    #Create Function
    def __init__(self, email, username, password, DateOfBirth, CNIC, Address, Phone_No, Employee_Type):
        self.E1 = EmployeeSerializer(email, username, password, DateOfBirth, CNIC, Address, Phone_No, Employee_Type)