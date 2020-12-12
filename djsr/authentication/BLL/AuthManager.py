from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import MyTokenObtainPairSerializer


class ObtainTokenPairWithAccountsView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)