from abc import abstractmethod
from ..views import ObtainTokenPairWithAccountsView , Register_Member
from rest_framework_simplejwt import views as jwt_views


class AbsAccountHandler:
    
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def refresh(self):
        pass
        

class AccountHandler(AbsAccountHandler):
    def login(self):
        return ObtainTokenPairWithAccountsView.as_view()

    def refresh(self):
        return jwt_views.TokenRefreshView.as_view()

    def create(self):
        return Register_Member.as_view()


        