from abc import abstractmethod

from .BLL.MemberManager import MemberManager
from .BLL.MembershipManager import MembershipManager
from .BLL.EmployeeManager import EmployeeManager
from .BLL.BillingManager import BillingManager

from .BLL.AuthManager import ObtainTokenPairWithAccountsView, LogoutAndBlacklistRefreshTokenForUserView

from rest_framework_simplejwt import views as jwt_views

class AbsApiCaller:
    
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

class MemberAccountApiCaller(AbsApiCaller):    

    def __init__(self):
        
        self.MemberMan = MemberManager()
        self.MembershipMan = MembershipManager()
        self.BillingMan = BillingManager()

        self.MemberMan.initializeManagers(self.MembershipMan)
        self.MembershipMan.initializeManagers(self.BillingMan)

    def signup(self):
        return self.MemberMan.registerMember()

    def deregister(self):
        return self.MemberMan.deregisterMember()

class EmployeeAccountApiCaller(AbsApiCaller):

    def __init__(self):
        self.EmployeeMan = EmployeeManager()

    def signup(self):
        return self.EmployeeMan.registerEmployee()
