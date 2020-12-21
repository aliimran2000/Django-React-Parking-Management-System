from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import MemberAccountApiCaller, EmployeeAccountApiCaller

#GLOBAL VARIABLES
EmpAccountApiCaller = EmployeeAccountApiCaller()
MemAccountApiCaller = MemberAccountApiCaller()

urlpatterns = [
    path('member/signup/', MemAccountApiCaller.signup(), name="Register_Member"),
    path('member/login/', MemAccountApiCaller.login(), name='member_token_create'),
    path('member/deregister/', MemAccountApiCaller.deregister(), name="Deregister_Member"),
    path('employee/signup/', EmpAccountApiCaller.signup(), name="Register_Employee"),
    path('employee/login/', EmpAccountApiCaller.login(), name='employee_token_create'),
    path('logout/',EmpAccountApiCaller.logout(),name="logout"),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]