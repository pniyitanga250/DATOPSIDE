
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include myapp URLs for authentication
    path('products/', include('products.urls')),
    path('payments/', include('payments.urls')),
    path('tools/', include('tools_and_opps.urls', namespace='tools_and_opps')),
    



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
