from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        # Only create a new profile if it doesn't exist
        UserProfile.objects.get_or_create(user=instance)
    else:
        # Update the profile for an existing user (if necessary)
        instance.userprofile.save()
