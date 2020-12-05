from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView
from .views import AccountsCreate

urlpatterns = [

    path('user/create/', AccountsCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

#curl --header "Content-Type: application/json" -X POST http://localhost:8000/api/user/create/ --data '{"email":"i181561@nu.edu.pk","username":"nomanaziz","password":"konnichiwa"}'
#{"email":"ichiro@mariners.com","username":"ichiro1"}