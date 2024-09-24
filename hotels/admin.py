from django.contrib import admin
from .models import Restaurant,Service,Food

# Register your models here.


@admin.register (Restaurant)
class PostAdmin(admin.ModelAdmin):
      list_display = ['name','photo']
      list_filter = ['name']
      ordering = ['name']


@admin.register(Service)
class PostAdmin(admin.ModelAdmin):
     list_display = ['service_name','service_price']
     list_filter = ['service_name','service_price']
     ordering = ['service_name']
    
@admin.register(Food)
class PostAdmin(admin.ModelAdmin):
      list_display = ['food_name','food_photo','food_price']
      list_filter = ['food_name','food_photo', 'food_price']
      ordering = ['food_name']



##class PostAdmin(admin.ModelAdmin):
  #  list_display = ['']
  #  list_filter = ['name']
   # ordering = ['name']


#class PostAdmin(admin.ModelAdmin):
 #   list_display = ['name','photo', 'food_price']
  #  list_filter = ['name']
  #  ordering = ['name']

