from django.db import models

# Create your models here.
class restaurant(models.Model):
    name = models.CharField(max_length=30)
    photo =models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
   