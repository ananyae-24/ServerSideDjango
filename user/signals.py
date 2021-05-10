from django.contrib.auth.models import User
from user.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@ receiver(post_save, sender=User)
def save_Profile(sender, instance, **kwargs):
    instance.profile.save()
