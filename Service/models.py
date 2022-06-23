import email
from email.errors import MultipartInvariantViolationDefect
from pyexpat import model
from django.db import models

class Newsletter(models.Model):
   email = models.EmailField(max_length=254)
    
class Started(models.Model): 
    description = models.TextField()
    img = models.FileField()
    
    
class Sevice_details(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)


class TeamMember(models.Model):       
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    img = models.FileField()
    
    def __str__(self):
        return self.name
    
class Social_Team(models.Model): 
    social = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="social_team")      
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    url = models.URLField()
    
    def __str__(self):
        return self.social.name

    
class Footer(models.Model):   
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    fb_link = models.URLField()
    youtude_link = models.URLField()
    twitter_link = models.URLField()
    insta_link = models.URLField()
    linked_link = models.URLField() 
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quote(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    service = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    
    
# Create your models here.
