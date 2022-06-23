from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework import permissions


from django.conf import settings
from django.conf.urls.static import static 



from django.views.decorators.csrf import csrf_exempt
# from Service.schema import schema

from Site.urls_api import router as Site_router

#This is for the api rest  
router = routers.DefaultRouter()
router.registry.extend(Site_router.registry)

#this is for the graphly part.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Site.urls')),
    path('rest/', include(router.urls)),
    # path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    
]

if settings.DEBUG:          
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)