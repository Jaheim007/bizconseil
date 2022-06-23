from django.db import models

class Site_Info(models.Model):
    section_testimonial_title = models.CharField(max_length=255)
    section_banner_title = models.CharField(max_length=255)
    section_about_title = models.CharField(max_length=255)
    section_features_title = models.CharField(max_length=255)
    section_team_title = models.CharField(max_length=255)
    section_service_title = models.CharField(max_length=255)
    section_started_title = models.CharField(max_length=255)
    site_logo = models.CharField(max_length=255)
    
    
class Banner(models.Model):        
    description = models.TextField()
    img = models.FileField() 



class About(models.Model):       
    description = models.TextField()
    img = models.FileField()

class AboutDetails(models.Model):
    title =  models.CharField(max_length=255)
    description = models.TextField()
    img = models.CharField(max_length=255)
    
class Features(models.Model):      
    description = models.TextField()
    
class Features_Details(models.Model):      
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.CharField(max_length=255)
    
class Slider(models.Model):     
    img = models.FileField()
    
class Testimonial(models.Model):       
    description = models.TextField()
    client_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    img = models.FileField() 
    
  

    
# Create your models here.
