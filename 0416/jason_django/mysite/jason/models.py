from django.db import models

# Create your models here.
class Introduction (models.Model):
	name = models.CharField(max_length=20)
	birthday = models.CharField(max_length=15)
	gender = models.CharField(max_length=10)

	def __str__(self):
		return self.name