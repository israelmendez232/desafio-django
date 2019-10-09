from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static
from .views import index, cadastro, login, area, areaInfo, pagina404, areaCurso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cadastro/', cadastro),
    path('login/', login), 
    path('area-do-aluno/', area),
    path('area-do-aluno-info/', areaInfo),
    path('pagina-nao-encontrada/', pagina404),
    path('area-do-aluno/<int:id>/', areaCurso, name = "id"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Administração para Professores'
admin.site.index_title = 'Altere/Crie os Cursos'
admin.site.site_title = 'Estratégia Vestibulares'
