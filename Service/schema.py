# # import graphene
# # from graphene_django import DjangoObjectType
# from .models import Contact, Newsletter, Quote

# class List_Contact(DjangoObjectType):
    
#     class Meta:
#         model = Contact
#         fields = ('name', 'email', 'subject', 'message')
        
# class List_Quote(DjangoObjectType):
    
#     class Meta:
#         model = Quote
#         fields = ('name', 'email', 'service', 'comment')
        
# class Newsletter(DjangoObjectType):
    
#     class Meta:
#         model = Newsletter
#         fields = ('email',)
        
# class Query(graphene.ObjectType):
#     all_contact = graphene.List(List_Contact)
#     all_quote = graphene.List(List_Quote)
#     all_newsletter = graphene.List(Newsletter)
    
#     def resolve_all_contact(root, info):
#         return Contact.objects.all()
    
#     def resolve_all_quote(root, info):
#         return Quote.objects.all()

 
# schema = graphene.Schema(query=Query)