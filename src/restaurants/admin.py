from django.contrib import admin
from .models import RestaurantLocation

# Register your models here.

# class RestaurantLocation(admin.ModelAdmin):
#     readonly_fields = ('timestamp',)


admin.site.register(RestaurantLocation)