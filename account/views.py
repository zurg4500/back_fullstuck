from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer, PasswordChange, PasswordDropSerializer, ChangeForgottenPassword
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class RegistrarionView(CreateAPIView):
    serializer_class = RegistrationSerializer 


class ActivationView(CreateAPIView):
    serializer_class = ActivationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response(
            {'message': 'Аккаунт успешно активирован'},
            status=status.HTTP_201_CREATED
            )

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        print(request.user.username)
        Token.objects.get(user=request.user).delete()
        return Response(
            {'message': 'Logged Out'},
            status=status.HTTP_204_NO_CONTENT
        )
    
class PasswordChangeView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChange

    def post(self, request, *args, **kwargs):
        serializer = PasswordChange(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response({'message': 'Пароль успешно обновлён'}, status=status.HTTP_200_OK)
     

class DropPasswordView(CreateAPIView):
    serializer_class = PasswordDropSerializer

    def post(self, request, *args, **kwargs):
        serializer = PasswordDropSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_activation_code()
        return Response({'message': 'Activation code was send'}, status=status.HTTP_200_OK)
    

class ChangeForgottenPasswordView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = ChangeForgottenPassword(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response({'message': 'Password was changed sucsessfuly'}, status=status.HTTP_201_CREATED)
    

