
from django.contrib import admin
from django.urls import path, include  # Make sure include is imported
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),  # Include store app urls
    path('', lambda request: redirect('/store/', permanent=True)),  # Redirect root URL to /store/

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)