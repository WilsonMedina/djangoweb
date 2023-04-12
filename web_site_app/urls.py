from django.urls import path
#------------------------------Own files----------------------------------------------#
from .views import AboutView, ExperienceView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('experience/', ExperienceView.as_view(), name='experience'),
]
