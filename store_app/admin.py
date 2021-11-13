from django.contrib import admin

from .models import Client, Product, Command

# Register your models here.
admin.site.register([Product,Client,Command])
#admin.site.register(Client)