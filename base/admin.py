from django.contrib import admin
from .models import Client, Guest, Teacher

# Register your models here.
admin.site.register(Client),
admin.site.register(Guest),
admin.site.register(Teacher),