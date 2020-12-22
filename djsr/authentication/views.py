from abc import abstractmethod

from rest_framework_simplejwt import views as jwt_views

from .apiView import initializeManagers
from .apiView import LogoutAndBlacklistRefreshTokenForUserView, ObtainTokenPairWithAccountsView
from .apiView import registerMemberApiView, deregisterMemberApiView, renewMembershipApiView, verifyCredentialsApiView, memberDetailsApiView
from .apiView import registerEmployeeApiView
from .apiView import registerVehicleApiView, deregisterVehicleApiView
from .apiView import accountNameApiView, accountTypeApiView

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

    def signup(self):
        return registerMemberApiView.as_view()

    def deregister(self):
        return deregisterMemberApiView.as_view()

    def verifyCredentials(self):
        return verifyCredentialsApiView.as_view()

    def registerVehicle(self):
        return registerVehicleApiView.as_view()

    def deregisterVehicle(self):
        return deregisterVehicleApiView.as_view()
 
    def getDetails(self):
        return memberDetailsApiView.as_view()

    def renewMembership(self):
        return renewMembershipApiView.as_view()

class EmployeeAccountApiCaller(AbsApiCaller):

    def __init__(self):
        
        initializeManagers()

    def signup(self):
        return registerEmployeeApiView.as_view()

    def getType(self):
        return accountTypeApiView.as_view()

    def getName(self):
        return accountNameApiView.as_view()