from .Employee import Employee

from ..modelManager import getEmployeeType

class EmployeeManager:

    def registerEmployee(self, email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type):
        
        Employee(email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type)

    def getEmployeeType(self, accountId):

        empType = getEmployeeType(accountId)
        return empType