from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithAccountsView,Register_Member
#from .BLL.accounthandler import AccountHandler


urlpatterns = [
    path('signup/', Register_Member.as_view(), name="Register_Member"),
    #path('account/create/employee', EmployeeCreate.as_view(), name="employee_create"),   
    path('signin/', ObtainTokenPairWithAccountsView.as_view(), name='token_create'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


# urlpatterns = [
#     path('signup/', ACC.create(), name="Register_Member"),
#     #path('account/create/employee', EmployeeCreate.as_view(), name="employee_create"),   
#     path('signin/', ACC,login(), name='token_create'),
#     path('refresh/', ACC.refresh(), name='token_refresh'),
# ]


