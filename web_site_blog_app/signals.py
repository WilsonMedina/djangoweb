from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
#-----------------------------------Own files-----------------------------------------------#
from .models import ProfileAuthor

#-------------------------Funtion that links a record to a user profile-----------------------------------------------#
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileAuthor.objects.create(author=instance)