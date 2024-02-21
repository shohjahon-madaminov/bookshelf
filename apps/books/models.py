from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User


class Book(BaseModel):
    class Status(models.TextChoices):
        new = 'New', 'new'
        reading = 'Reading', 'reading'
        fimished = 'Finished', 'fimished'
        
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    pages = models.IntegerField()
    isbn = models.IntegerField(unique=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.new)
    
    published = models.DateField()
    started_time = models.DateField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title
    