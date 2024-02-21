from celery import shared_task

from apps.users.models import User, UserProfile

import time

@shared_task
def create_userprofile_task(user_id):
    user = User.objects.get(pk=user_id)
    UserProfile.objects.create(user=user)
    time.sleep(10)
