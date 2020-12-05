from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView
from .views import AccountsCreate , EmployeeCreate

urlpatterns = [
    path('account/create/', AccountsCreate.as_view(), name="account_create"),
    path('account/create/employee', EmployeeCreate.as_view(), name="employee_create"),   
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

#curl --header "Content-Type: application/json" -X POST http://localhost:8000/api/user/create/ --data '{"email":"i181561@nu.edu.pk","username":"nomanaziz","password":"konnichiwa"}'
#{"email":"ichiro@mariners.com","username":"ichiro1"}


'''
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwODQwNTA5MSwianRpIjoiZmY1YzA5ZGI4MzEyNGY1MmIwZDA3MzBlMGU1OTgyNTMiLCJ1c2VyX2lkIjoxfQ.DgtZHCNcAIwpwee8bNCO-mqguBCec9yzGLCGKI-esRk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MTk1NzkxLCJqdGkiOiI3NTNiYjk5NmZiZTA0ZTIzOWI3YTc2MjljMjJlZDhjMCIsInVzZXJfaWQiOjF9.3JTNDEJ0AZtujicv_WSTZduxPwujczbdlpaL3k6cUOE"
}
'''

