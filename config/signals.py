from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User
from config.tasks import create_userprofile_task

@receiver(post_save, sender=User)
def run_userprofile_task(sender, instance, created, **kwargs):
    if created:
        create_userprofile_task.delay(instance.id)