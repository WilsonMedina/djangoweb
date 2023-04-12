from django.urls import path
#-----------------------------------Own files-----------------------------------------------#
from .views import RegisterView, LoginView, ResetPasswordView, logout_view, activate, reset_password_activate

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
     path("reset-password/", ResetPasswordView.as_view(), name="reset_password"),
    path('reset-password-activate/<uidb64>/<token>/', reset_password_activate, name='reset_password_activate'),
]