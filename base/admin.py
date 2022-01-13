from django.contrib import admin
from .models import Client, Guest, Teacher, Job

# Register your models here.
admin.site.register(Client),
admin.site.register(Guest),
admin.site.register(Teacher),
admin.site.register(Job),