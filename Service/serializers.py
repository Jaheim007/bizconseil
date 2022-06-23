from rest_framework import serializers
from .models import Contact, Newsletter, Quote

class ContactSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
class QuoteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Quote
        fields = '__all__'
        
class NewsletterSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Newsletter
        fields = '__all__'
        
