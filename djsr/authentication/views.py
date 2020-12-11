from abc import abstractmethod
from .BLL.MemberManager import Register_Member_Request
from .BLL.Accounthandler import ObtainTokenPairWithAccountsView, Deregister_Member, Register_Employee , LogoutAndBlacklistRefreshTokenForUserView
from rest_framework_simplejwt import views as jwt_views

class AbsAccountHandler:
    
    def login(self):
        return ObtainTokenPairWithAccountsView.as_view()
    
    def logout(self):
        return LogoutAndBlacklistRefreshTokenForUserView.as_view()


    @abstractmethod
    def signup(self):
        pass

    @abstractmethod
    def deregister(self):
        pass
    
    def refresh(self):
        return jwt_views.TokenRefreshView.as_view()



class MemberAccountHandler(AbsAccountHandler):    

    def signup(self):
        return Register_Member_Request.as_view()

    def deregister(self):
        return Deregister_Member.as_view()

class EmployeeAccountHandler(AbsAccountHandler):

    def signup(self):
        return Register_Employee.as_view()
