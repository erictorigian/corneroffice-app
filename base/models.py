from django.db import models

# Create your models here.
class Client(models.Model):
    contact = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    source = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200)
    comments = models.TextField()
    #auto time fields
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.contact