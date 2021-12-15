from django.db import models
import uuid
# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key = True, editable = False, unique = True, default = uuid.uuid4)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.title