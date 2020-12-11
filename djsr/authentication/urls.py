from django.urls import path
from rest_framework_simplejwt import views as jwt_views
#from .views import ObtainTokenPairWithAccountsView,Register_Member
from .views import MemberAccountHandler, EmployeeAccountHandler , LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [
    path('member/signup/', MemberAccountHandler().signup(), name="Register_Member_Request"),
    path('member/login/', MemberAccountHandler().login(), name='member_token_create'),
    path('member/deregister/', MemberAccountHandler().deregister(), name="Deregister_Member"),
    path('employee/signup/', EmployeeAccountHandler().signup(), name="Register_Employee"),
    path('employee/login/', EmployeeAccountHandler().login(), name='employee_token_create'),
    path('logout/',LogoutAndBlacklistRefreshTokenForUserView().as_view(),name="logout"),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


# urlpatterns = [
#     path('signup/', ACC.create(), name="Register_Member"),
#     #path('account/create/employee', EmployeeCreate.as_view(), name="employee_create"),   
#     path('signin/', ACC,login(), name='token_create'),
#     path('refresh/', ACC.refresh(), name='token_refresh'),
# ]


