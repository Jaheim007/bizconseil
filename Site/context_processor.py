from Service.models import Footer

def Footer_details(request):      
    footer = Footer.objects.all()
    
    return{
        'footer': footer
    }