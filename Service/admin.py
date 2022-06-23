from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Newsletter, Social_Team, Started, Footer, TeamMember, Sevice_details, Contact, Quote

@admin.register(Newsletter)
class News(admin.ModelAdmin):          
    list_display = ('email', )

@admin.register(Contact)
class Contact(admin.ModelAdmin):          
    list_display = ('name','email' )
    
    
@admin.register(TeamMember)
class TeamMember(admin.ModelAdmin):           
    list_display = ('views','name',)

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 


@admin.register(Social_Team)
class Social_Team(admin.ModelAdmin):          
    list_display = ('name','icon', 'url' )
    
@admin.register(Started)
class Start(admin.ModelAdmin):          
    list_display = ('views', 'description')

    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'
    
    
@admin.register(Footer)
class Footer(admin.ModelAdmin):        
    list_display = ('title', 'email', 'address', 'phone')

@admin.register(Sevice_details)
class Service(admin.ModelAdmin):        
    list_display = ('title', 'description', 'img1', 'img2')

@admin.register(Quote)
class Quote(admin.ModelAdmin):        
    list_display = ('name', 'email', 'service', 'comment')

# Register your models here.
