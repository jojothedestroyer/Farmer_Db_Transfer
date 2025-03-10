
from django.contrib import admin
from django.urls import path, include
from django.conf import  settings 
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gcna_data.urls')),
    path('', include('pwa.urls')),
    re_path(r'^pwa/', include('pwa.urls')),
    path('manifest.json', TemplateView.as_view(template_name='manifest.json', content_type='application/json')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
