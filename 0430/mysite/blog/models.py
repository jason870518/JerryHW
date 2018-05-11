# Create your models here.
from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


