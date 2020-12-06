from abc import abstractmethod
from ..views import ObtainTokenPairWithAccountsView , Register_Member, Register_Employee
from rest_framework_simplejwt import views as jwt_views


class AbsAccountHandler:
    
    def login(self):
        return ObtainTokenPairWithAccountsView.as_view()

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def signup(self):
        pass

    @abstractmethod
    def refresh(self):
        pass
        

class MemberAccountHandler(AbsAccountHandler):
        
    def refresh(self):
        return jwt_views.TokenRefreshView.as_view()

    def signup(self):
        return Register_Member.as_view()



class EmployeeAccountHandler(AbsAccountHandler):

    def refresh(self):
        return jwt_views.TokenRefreshView.as_view()

    def signup(self):
        return Register_Employee.as_view()
