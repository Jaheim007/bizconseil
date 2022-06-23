from django import views
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Banner, About, AboutDetails, Features_Details, Site_Info, Slider, Testimonial
from Service.models import Newsletter, Started, Sevice_details, TeamMember, Newsletter, Social_Team, Contact, Quote
from Service.serializers import ContactSerializers, NewsletterSerializers, QuoteSerializers


def index(request):   
    banner = Banner.objects.all()  
    about = About.objects.all()  
    about_details = AboutDetails.objects.all()
    Start = Started.objects.all()
    features_details = Features_Details.objects.all()
    img = Slider.objects.all()
    section = Site_Info.objects.first()
    service = Sevice_details.objects.all()
    testimonial = Testimonial.objects.all()
    team = TeamMember.objects.all() 
    social_team = Social_Team.objects.all()
         
    
    if request.method == "POST":
        email = request.POST.get('email')
        news = Newsletter(email = email)
        news.save()
        
            
    return render(request, 'pages/index.html', locals())

    
def about(request):  
    about_details = AboutDetails.objects.all()     
    features_details = Features_Details.objects.all()
    team = TeamMember.objects.all() 
    about = About.objects.all() 
    section = Site_Info.objects.first()

    return render(request, 'pages/about.html', locals())

def error(request): 
    section = Site_Info.objects.first()      
    return render(request, 'pages/404.html', locals())

def contact(request):  
    section = Site_Info.objects.first()  

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']  
        subject = request.POST['subject']  
        message = request.POST['message']
        contact = Contact(
            name = name, 
            email = email, 
            subject = subject , 
            message = message)

        contact.save()

    return render(request, 'pages/contact.html', locals())

def feature(request):   
    features_details = Features_Details.objects.all()  
    section = Site_Info.objects.first()  
    return render(request, 'pages/feature.html', locals())

def quote(request):  
    section = Site_Info.objects.first()   
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email') 
        service = request.POST.get('service')  
        comment = request.POST.get('comment')
        quote = Quote(
            name = name, 
            email = email, 
            service = service, 
            comment = comment)

        quote.save()
    

    return render(request, 'pages/quote.html', locals())

def team(request): 
    team = TeamMember.objects.all() 
    section = Site_Info.objects.first()      
    return render(request, 'pages/team.html', locals())

def testimonial(request):      
    testimonial = Testimonial.objects.all()  
    section = Site_Info.objects.first()
    return render(request, 'pages/testimonial.html', locals())

def service(request):   
    service = Sevice_details.objects.all()  
    testimonial = Testimonial.objects.all()  
    section = Site_Info.objects.first()
    return render(request, 'pages/service.html', locals())

#Doing Api Rest in the views.py     
class ContactViewsSet(viewsets.ModelViewSet):      
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

class QuoteViewsSet(viewsets.ModelViewSet):      
    
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

class NewsletterViewsSet(viewsets.ModelViewSet):      
    
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializers
    

    



# Create your views here.
