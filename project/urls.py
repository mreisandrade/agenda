"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Usada para concatenar as urls das imagens
from django.conf.urls.static import static
# Importa as configurações de settings.py, já que este 
# módulo não pode ser importado diretamente
from django.conf import settings


urlpatterns = [
    # Cria a url home do site (app contact)
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
]

# Configurando os links das imagens
urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT, 
)
# Configurando os links para os arquivos estáticos
urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT, 
)
