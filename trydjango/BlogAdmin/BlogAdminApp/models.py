from django.db import models

# Create your models here.

class CreateStoryHeader(models.Model):
	title 		= models.CharField(max_length=100)
	one_liner	= models.CharField(max_length=150 )
