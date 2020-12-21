from abc import abstractmethod

from rest_framework_simplejwt import views as jwt_views

from .apiView import initializeManagers
from .apiView import LogoutAndBlacklistRefreshTokenForUserView, ObtainTokenPairWithAccountsView
from .apiView import registerMemberApiView, deregisterMemberApiView
from .apiView import registerEmployeeApiView

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

class EmployeeAccountApiCaller(AbsApiCaller):

    def __init__(self):
        
        initializeManagers()

    def signup(self):
        return registerEmployeeApiView.as_view()