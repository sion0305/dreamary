from django.contrib import admin
from django.urls import path, include
from DreamaryApp import views
import DreamaryApp.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('DreamaryApp/', include(DreamaryApp.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
