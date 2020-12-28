from .Employee import Employee

from ..modelManager import getEmployeeObject

class EmployeeManager:

    def registerEmployee(self, email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type):
        
        Employee(email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type)

    def getEmployeeById(self, employeeId):

        return getEmployeeObject(employeeId)
