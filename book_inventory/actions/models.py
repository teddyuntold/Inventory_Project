<<<<<<< HEAD
from django.db import models

# Create your models here.
class Actions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
=======
from django.db import models

# Create your models here.
class Actions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
>>>>>>> 59d377753d1f1b0d186c349bc7c3a802a07a04c2
        return self.title