from django.urls import path
from rest_framework_simplejwt import views as jwt_views
#from .views import ObtainTokenPairWithAccountsView,Register_Member
from .views import MemberAccountApiCaller, EmployeeAccountApiCaller , LogoutAndBlacklistRefreshTokenForUserView

MemAccountApiCaller = MemberAccountApiCaller()
EmpAccountApiCaller = EmployeeAccountApiCaller()

urlpatterns = [
    path('member/signup/', MemAccountApiCaller.signup(), name="Register_Member"),
    path('member/login/', MemAccountApiCaller.login(), name='member_token_create'),
    path('member/deregister/', MemAccountApiCaller.deregister(), name="Deregister_Member"),
    path('employee/signup/', EmpAccountApiCaller.signup(), name="Register_Employee"),
    path('employee/login/', EmpAccountApiCaller.login(), name='employee_token_create'),
    path('logout/',LogoutAndBlacklistRefreshTokenForUserView().as_view(),name="logout"),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


# urlpatterns = [
#     path('signup/', ACC.create(), name="Register_Member"),
#     #path('account/create/employee', EmployeeCreate.as_view(), name="employee_create"),   
#     path('signin/', ACC,login(), name='token_create'),
#     path('refresh/', ACC.refresh(), name='token_refresh'),
# ]


