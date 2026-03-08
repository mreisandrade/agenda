from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    # Caminho padrão a partir do contact/
    path('', views.index, name='index'),
]