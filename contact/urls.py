from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    # Vizualização do contato
    path('<int:contact_id>/', views.contact, name='contact'),
    # Caminho padrão a partir do contact/
    path('', views.index, name='index'),
]