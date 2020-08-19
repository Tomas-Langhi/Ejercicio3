from django.db import models

# Create your models here.
class Libro(models.Model):
    editorial = models.CharField(max_length=50, default="");
    