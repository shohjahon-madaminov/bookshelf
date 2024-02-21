from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.models import User
from apps.users import serializers


class SignUpAPIView(CreateAPIView):
    serializer_class = serializers.SignUpSerializer
    queryset = User.objects.all()
    
    
class LoginAPIView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer
    
    
class LogOutAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def post(self, request):
        serializer = serializers.LogOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh = request.data['refresh']
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(
                {
                    'success': True,
                    'message': "you have successfully logged out",
                    'status': status.HTTP_205_RESET_CONTENT                    
                }
            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class LoginRefreshAPIVIew(TokenRefreshView):
    serializer_class = serializers.LoginRefreshSerializer
    
    
# class UserProfileAPIView(RetrieveAPIView):
#     serializer_class = serializers.UserSerializer
#     queryset = User.objects.filter()

class UserProfileAPIView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = serializers.UserSerializer(user)
            return Response({
                'data': serializer.data, 'status': status.HTTP_200_OK
            })
        except User.DoesNotExist:
            return Response({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})