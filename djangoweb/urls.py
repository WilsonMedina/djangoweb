from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('public/', include(('web_site_app.urls', 'website'))),
    path('', include(('web_site_blog_app.urls', 'blog'))),
    path('accounts/', include(('web_site_auth_app.urls', 'auth'))),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
