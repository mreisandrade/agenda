from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    # Caminho padrão a partir do contact/
    path('', views.index, name='index'),
    # Vizualização dos contatos filtrados pela pesquisa
    path('search/', views.search, name='search'),

    # Como é padronizado a criação de URLs
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'), # Leitura 
    path('contact/create/', views.create, name='create'), # Criação
    path('contact/<int:contact_id>/update/', views.update, name='update'), # Atualizando 
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), # Deletar 

    # Exemplo para dados dos usuários
    # users (CRUD)
    # path('users/<int:contact_id>/detail/', views.contact, name='contact'), # Leitura 
    # path('users/create/', views.contact, name='contact'), # Criação
    # path('users/<int:contact_id>/update/', views.contact, name='contact'), # Atualizando 
    # path('users/<int:contact_id>/delete/', views.contact, name='contact'), # Deletar 
]
