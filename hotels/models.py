from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    photo =models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
   
class Service(Restaurant):
    service_name = models.CharField(max_length=20)
    service_price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.service_name
    
class Food(Restaurant):
    food_name =models.CharField(max_length=20)
    food_photo = models.ImageField(upload_to='images/')
    food_price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.food_name
    
    
class Meta:
     ordering = ['-name']
     indexes =[
     models.Index(fields=['-name']),
     ]