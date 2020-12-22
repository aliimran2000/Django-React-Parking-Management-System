from .Employee import Employee

class EmployeeManager:

    def registerEmployee(self, email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type):
        
        Employee(email, username, password, DateOfBirth, Cnic, Address, Phone_No, Employee_Type)
