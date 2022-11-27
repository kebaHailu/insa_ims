from django.contrib.auth.models import User 
from .models import Profile 
from django.db.models.signals import post_save 
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_Profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(staff=instance)

def save_Profile(sender,instance,**kwargs):
    instance.profile.save()