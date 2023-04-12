
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, TemplateView
#------------------Own files----------------------------------------#
from .models import About, Experience

#-----------------Expirence----------------------------------------#  
class ExperienceView(SuccessMessageMixin, ListView):
    model = Experience
    template_name = 'experience.html'

    def get(self, request):
        expirence = self.model.objects.filter(state = True)
        if expirence:
            return render(self.request, self.template_name, {'experiences' :expirence})
        else:
            messages.add_message(self.request, messages.INFO, 'No hay nada por acá para mostrar')
            return redirect('blog:home_blog')
            

#------------------About---------------------------------------#
class AboutView(SuccessMessageMixin, TemplateView):
    model = About
    template_name = 'about.html'

    def get(self, request):
        about = self.model.objects.filter(state = True)
        if about:
            return render(self.request, self.template_name, {'about' :about})
        else:
            messages.add_message(self.request, messages.INFO, 'No hay nada por acá para mostrar')
            return redirect('blog:home_blog')
        




 
