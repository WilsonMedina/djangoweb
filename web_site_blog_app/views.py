from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
#-----------------------------------Own files-----------------------------------------------#
from .models import ProfileAuthor, Category, Post
from .forms import PostForm, PhotoForm, ProfileForm

#-------------------------------------------Home-----------------------------------------------#
class HomeBlogView(SuccessMessageMixin, ListView):
    model = Post
    model2 = Category
    template_name = 'home_blog.html'
    
    def get(self, request):
        queryset = request.GET.get('search')
        posts = self.model.objects.filter(state = True)
        categories = self.model2.objects.filter(state = True)
        if queryset:
            posts = self.model.objects.filter(
                Q(title__icontains = queryset) |
                Q(excerpt__icontains = queryset) |
                Q(content__icontains = queryset)  
            ).distinct()
        paginator = Paginator(posts, 4)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        if posts:
            return render(request, self.template_name, {'posts' : posts, 'categories' : categories})
        else:
            messages.add_message(self.request, messages.INFO, 'No hay post para mostrar.')
            return render(request, self.template_name, {'posts' : posts, 'categories' : categories})
        
#-------------------------------------------Read post-----------------------------------------------#    
class ReadPostView(ListView):
    template_name = 'read_post.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk = pk)
        return render(request, self.template_name, {'post' : post})
    
#-------------------------------------------List posts for category-----------------------------------------------#    
class ListPostsView(SuccessMessageMixin, ListView):
    model = Post
    model2 = Category
    template_name = 'list_posts.html'

    def get(self, request, pk):
        posts = self.model.objects.filter(state = True, category = pk)
        category = self.model2.objects.get(pk = pk)
        paginator = Paginator(posts, 4)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        if posts:
            return render(request, self.template_name, {'posts' : posts, 'category' : category})
        else:
            messages.add_message(self.request, messages.INFO, 'En esta categoria no hay posts para mostrar.')
            return redirect('blog:home_blog')
        
#-------------------------------------------Dashboard-----------------------------------------------#
class DashboardView(ListView):
    model = Post
    model2 = ProfileAuthor
    template_name = 'dashboard.html'

    def get(self, request):
        current_user = get_object_or_404(User, pk = request.user.pk) 
        posts = self.model.objects.filter(state = True, author_id = current_user)
        profile = self.model2.objects.get(author_id = current_user)
        message = 'No tienes posts para mostrar.'
        return render(request, self.template_name, {'posts' : posts, 'profile' : profile, 'message' : message})
    
#-------------------------------------------Create post-----------------------------------------------#    
class CreatePostView(SuccessMessageMixin, CreateView):
    form_class = PostForm
    template_name = 'create_post.html'
   
    def form_valid(self, form):
        current_user = self.request.user.pk
        post = form.save(commit=False)
        post.author_id = current_user
        post.save()
        author = self.request.user.username + ' ' + 'Creo un post'
        title = self.request.POST['title'] + ' ' + self.request.user.username + ' ' + self.request.POST['category']
        email_from = settings.EMAIL_HOST_USER
        email_to = ['wilson.89medina@gmail.com']
        send_mail(author, title, email_from, email_to)
        messages.add_message(self.request, messages.SUCCESS, '¡Tu post se creo correctamente, será evaluado y públicado!')
        return redirect('blog:dashboard')
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Todos los campos son obligatorios.')
        return render(self.request, self.template_name, {'form' : form})
    
#-------------------------------------------Update post-----------------------------------------------# 
class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.state = False
        post.save()
        author = self.request.user.username + ' ' + 'Actualizó un post'
        title = self.request.POST['title']
        email_from = settings.EMAIL_HOST_USER
        email_to = ['wilson.89medina@gmail.com']
        send_mail(author, title, email_from, email_to)
        messages.add_message(self.request, messages.SUCCESS, '¡Tu post se actualizo correctamente, será evaluado y públicado!')
        return redirect('blog:dashboard')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Todos los campos son obligatorios.')
        return render(self.request, self.template_name, {'form' : form})
    
#-------------------------------------------Update photo-----------------------------------------------#
class UpdatePhotoView(SuccessMessageMixin, UpdateView):
    model = ProfileAuthor
    template_name = 'update_photo.html'
    form_class = PhotoForm
    success_url = reverse_lazy('blog:dashboard')
    success_message = '¡Tu Foto se actualizo correctamente!'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'El archivo no corresponde a una imagen.')
        return render(self.request, self.template_name, {'form' : form})
    
#-------------------------------------------Update profile-----------------------------------------------#    
class UpdateProfileView(SuccessMessageMixin ,UpdateView):
    model = User
    template_name = 'update_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('blog:dashboard')
    success_message = '¡Tu perfil se actualizo correctamente!'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'El usuario y/o correo electronico ya existe en otro usuario.')
        return render(self.request, self.template_name, {'form' : form})
    
#-------------------------------------------Delete post-----------------------------------------------#    
class DeletePostView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('blog:dashboard')
    success_message = '¡Tu post se eliminó correctamente!'
    

    
