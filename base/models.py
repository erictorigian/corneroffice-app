from django.db import models

STATUS_CHOICES = (
    ('active', 'ACTIVE'),
    ('quoted', 'QUOTED'),
    ('prospect', 'PROSPECT'),
)
# Create your models here.
class Client(models.Model):
    contact = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    source = models.CharField(max_length = 200)
    status = models.CharField(max_length = 10, choices=STATUS_CHOICES, default="prospect")
    comments = models.TextField()
    #auto time fields
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.contact

class Guest(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    topic = models.TextField()
    show_date = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=200)
    comments = models.TextField()
    sponsor = models.IntegerField("Guest Sponsor",blank=False, default=1)
    updated = models.DateTimeField(auto_now=True)
    created =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    topics = models.CharField(max_length=200)
    sponsor = models.IntegerField("Teacher Sponsor", blank=False)
    updated = models.DateTimeField(auto_now=True)
    created =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.first_name + " " + self.last_name