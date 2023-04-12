from django import forms
from django.contrib.auth.models import User
#-----------------------------------Own files-----------------------------------------------#
from .models import Post, ProfileAuthor

#-----------------------------------Form create and update post-----------------------------------------------#
class PostForm(forms.ModelForm):
    title = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Titulo del Post*'}))
    excerpt = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Corta introduccion al post*'}))
    
    class Meta:
        model = Post
        exclude = ['created', 'state', 'timestamp', 'author', 'state']
        fields = ['title', 'excerpt', 'image', 'content', 'category']
        labels = {
            'image' : 'Imagen',
            'content' : 'Contenido',
            'category' : 'Categoria',
        }

#-----------------------------------Form update photo----------------------------------------------#      
class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='')

    class Meta:
        model = ProfileAuthor
        exclude = ['author']

#-------------------------------------Form update profile-----------------------------------------------#
class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Nombre de usuario'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Nombres'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder' : 'Apellidos'}))
    email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'placeholder' : 'Correo electronico'}))

    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups']
