from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('noticias/', include('noticias.urls')),
    path("admin/", admin.site.urls),
]
