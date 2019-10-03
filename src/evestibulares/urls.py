from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, cadastro, login, area, areaInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cadastro/', cadastro),
    path('login/', login),
    path('area-do-aluno/', area),
    path('area-do-aluno-info/', areaInfo),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
