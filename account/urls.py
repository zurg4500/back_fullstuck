from django.urls import path
from .views import RegistrarionView, ActivationView, LoginView, LogoutView, PasswordChangeView, DropPasswordView, ChangeForgottenPasswordView

 
urlpatterns = [
    path('registration/', RegistrarionView.as_view(), name = 'registration'),
    path('activate/', ActivationView.as_view(), name = 'activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(), name='change-password'),
    path('drop-password/', DropPasswordView.as_view(), name='drop-password'),
    path('set-new-password/', ChangeForgottenPasswordView.as_view, name='set-new-password')
]