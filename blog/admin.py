from django.contrib import admin
from .models import post,BlogComments

# Register your models here.
admin.site.register((post,BlogComments))
