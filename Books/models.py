from django.db import models
import uuid
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True) 
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    ShelfNo = models.IntegerField()

    def __str__(self):
        return self.Title