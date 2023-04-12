from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site 
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode   
from django.template.loader import render_to_string 
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user_model 
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
#-----------------------------------Own files-----------------------------------------------#
from .forms import UserCreateForm, UserAuthForm, ResetPasswordForm, SetPasswordForm
from .token import account_activation_token  

#---------------------------------------Login-----------------------------------------------#
class LoginView(SuccessMessageMixin, FormView):
    template_name = 'login.html'
    form_class = UserAuthForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(self.request, user)
            return redirect('blog:dashboard')
        else:
            messages.add_message(self.request, messages.ERROR, 'Ingreso invalido, usuario no existe')
            return redirect('auth:login')
        
    def form_invalid(self, form):
       messages.add_message(self.request, messages.ERROR, 'Ingreso invalido, datos incorrectos.')
       return render(self.request, self.template_name, {'form' : form})

#-------------------------------------------Register-----------------------------------------------#
class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        activate_email(self.request, user, form.cleaned_data.get('email'))
        messages.add_message(self.request, messages.SUCCESS, f'{user.username}: por favor confirma tu correo electronico para finalizar el registro!')
        return redirect('blog:home_blog')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'El usuario y/o correo electronico ya existe en otro usuario!')
        return render(self.request, self.template_name, {'form' : form})

#---------------------------------Register funtion activateEmail---------------------------------------------#       
def activate_email(request, user, to_email):
    subject = 'Activa tu cuenta!'
    message = render_to_string('email_activate.html', {
        'user' : user,
        'domain' : get_current_site(request).domain,
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token' : account_activation_token.make_token(user),
        'protocol' : 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(subject, message, to=[to_email])
    if email.send():
       pass
    else:
        messages.error(request, f'Hubo un problema para enviar el link de confirmacion a tu correo {to_email}')
        return redirect('auth:register')
        
#-------------------------------Register funtion activate-----------------------------------------------#
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Gracias por confirmar tu correo, ya puedes ingresar a tu cuenta!')
        userername = user.username 
        information = user.first_name + ' ' + user.last_name + ' ' + user.email
        email_from = settings.EMAIL_FROM
        email_to = ['wilson.89medina@gmail.com']
        send_mail(userername, information, email_from, email_to)
        return redirect('auth:login')
    
    messages.error(request, 'Este link ya fue usado, ya puede ingresar con sus credenciales')
    return redirect('auth:login')
    
#---------------------------------------Reset password--------------------------------------------# 
class ResetPasswordView(SuccessMessageMixin, FormView):
    template_name = 'reset_password.html'
    form_class = ResetPasswordForm

    def form_valid(self, form):
        user_email = form.cleaned_data['email']
        user = get_user_model().objects.filter(Q(email=user_email)).first()
        if user:
            subject = 'Recuperar clave!'
            message = render_to_string('reset_password_activate.html', {
                'user': user,
                'domain': get_current_site(self.request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'protocol': 'https' if self.request.is_secure() else 'http'
            })
            email = EmailMessage(subject, message, to=[user.email])
            if email.send():
                messages.add_message(self.request, messages.SUCCESS, f'{user.username}: hemos enviado instrucciones por correo electrónico para recuperar su clave, debería recibirlas en breve.')
                return redirect('blog:home_blog')
            else:
                messages.add_message(self.request, messages.ERROR, 'Hubo problema al enviar el correo electrónico, intentelo de nuevo.')
                return render(self.request, self.template_name, {'form' : form})
        else:
            messages.add_message(self.request, messages.ERROR, 'Correo no encontrado, por favor verifiquelo y escribalo correctamente.')
            return render(self.request, self.template_name, {'form' : form})

    def form_invalid(self, form):
       messages.add_message(self.request, messages.ERROR, 'Formulario de solicitud invalido, intentelo nuevamente.')
       return render(self.request, self.template_name, {'form' : form})

#---------------------------------------Reset password funtion reset activate--------------------------------------------# 
def reset_password_activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tu clave se recupero satisfactoriamente, ya puedes ingresar.')
                return redirect('auth:login')
            else:
                messages.error(request, 'Formulario de solicitud invalido, intentelo nuevamente.')
        else:
            form = SetPasswordForm(user)
            return render(request, 'confirmation_reset_password.html', {'form': form})
    else:
        messages.error(request, 'Hubo un problema en el registro intentalo de nuevo.')

    messages.error(request, 'Este link ya fue usado, genere uno nuevo en ¡Recuperar clave!')
    return redirect('auth:login')

#---------------------------------------Logout--------------------------------------------#  
def logout_view(request):
    logout(request)
    return redirect('blog:home_blog')
           
    
