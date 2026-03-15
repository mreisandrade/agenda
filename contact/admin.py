from django.contrib import admin
# Model criado no app Contact
from contact import models


# Register your models here.
# Criando a conexão do model Contact criado no app Contact
# Por padrão, o nome da classe é definido como 
#   NomeDoApp + Admin: NomeDoAppAdmin
# Para configurar o model, normalmente, usa-se o decorator 
# abaixo. Recebe como parâmentro o model criado.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Lista de campos mostrados na área admin
    # É um iterável (tupla ou lista)
    list_display = [
        # O id é criado automaticamente
        'id',
        'first_name',
        'last_name',
        'phone',
        'show',
    ]

    # Ordenando as listas
    # Colocar um menos (-) antes do campo, ordena de forma
    # descrescente (sem nada, é ordem crescente)
    ordering = [
        '-id',
    ]

    # Adiciona filtros
    # list_filter = [
    #     'created_date',
    # ]

    # Campos de pesquisa
    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    # Configura o número de contatos por página
    list_per_page = 10

    # Máximo de dados mostrados em "Mostrar Tudo"
    list_max_show_all = 200

    # Adiciona uma forma de editar os valores diretamente
    list_editable = [
        'first_name',
        'last_name',
        'show',
    ]

    # Torna aquele campo um link para abrir o dado
    # O mesmo campo não pode estar no list_editable e no
    # list_display_links ao mesmo tempo
    list_display_links = [
        'id',
        'phone',
    ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # Lista de campos mostrados na área admin
    # É um iterável (tupla ou lista)
    list_display = [
        # O id é criado automaticamente
        'id',
        'name',
    ]