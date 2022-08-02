import imp
from django.contrib import admin
from.models import Restaurants, Meals

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'type_of_food']
    

class MealAdmin(admin.ModelAdmin):
    list_display = ['meal_name', 'price', 'restaurants', 'image_url']
    
    
admin.site.register(Restaurants, RestaurantAdmin)
admin.site.register(Meals, MealAdmin)

