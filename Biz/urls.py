from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

from django.conf import settings
from django.conf.urls.static import static 



from django.views.decorators.csrf import csrf_exempt
# from Service.schema import schema

from Site.urls_api import router as Site_router

#This is for the api rest  
router = routers.DefaultRouter()
router.registry.extend(Site_router.registry)

#this is for the graphly part.
schema_view = get_schema_view(
      openapi.Info(
         title="Swagger Info",
         default_version='v1',
         description="Test description",
         terms_of_service="https://www.google.com/policies/terms/",
         contact=openapi.Contact(email="contact@snippets.local"),
         license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Site.urls')),
    path('rest/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    
]

if settings.DEBUG:          
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)