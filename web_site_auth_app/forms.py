from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#-----------------------------------Form register-----------------------------------------------#
class UserCreateForm(UserCreationForm):
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Nombre de usuario', 'autofocus' : 'true'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Nombres'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Apellidos'}))
    email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'placeholder' : 'Correo electronico'}))
    password1 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder' : 'Clave'}))
    password2 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder' : 'Confirma tu clave'}))
     
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k : '' for k in fields}

#------------------------------------Form login----------------------------------------------#
class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Nombre de usuario', 'autofocus' : 'true'}))
    password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder' : 'Clave'}))

    class Meta:
        model = User
        fields = ['username', 'password']

#--------------------------------------Form reset password-----------------------------------------------#
class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder' : 'Nueva clave', 'autofocus' : 'true'}))
    new_password2 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder' : 'Confirma tu nueva clave'}))

    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']
        help_texts = {k : '' for k in fields}

#-----------------------------------Form send email reset password-----------------------------------------------#
class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'placeholder' : 'Ingrese su correo electronico', 'autofocus' : 'true'}))

    class Meta:
        model = get_user_model()
        fields = ['email']
        
       