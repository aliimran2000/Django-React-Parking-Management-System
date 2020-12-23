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
    path('member/registervehicle/', MemAccountApiCaller.registerVehicle(), name="Register_Vehicle"),
    path('member/deregistervehicle/', MemAccountApiCaller.deregisterVehicle(), name="Deregister_Vehicle"),
    path('member/getdetails/', MemAccountApiCaller.getDetails(), name='get_member_details'),
    path('member/renewmembership/', MemAccountApiCaller.renewMembership(), name='renew_membership'),
    path('member/verifycredentials/', MemAccountApiCaller.verifyCredentials(), name='verify_credentials'),
    path('member/parkvehicle/', MemAccountApiCaller.parkVehicle(), name='park_vehicle'),
    path('member/exitvehicle/', MemAccountApiCaller.exitVehicle(), name='exit_vehicle'),

    path('account/getname/', EmpAccountApiCaller.getName(), name='get_account_name'),
    path('account/gettype/', EmpAccountApiCaller.getType(), name='get_account_type'),

    path('employee/signup/', EmpAccountApiCaller.signup(), name="Register_Employee"),
    path('employee/login/', EmpAccountApiCaller.login(), name='employee_token_create'),

    path('logout/',EmpAccountApiCaller.logout(),name="logout"),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]