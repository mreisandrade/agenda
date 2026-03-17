from django.shortcuts import render, get_object_or_404, redirect
# Importando o model dos contatos (database)
from contact.models import Contact
# Usado para levar a exceção de página não encontrada (Erro 404)
from django.http import Http404
# Classe para usar condições OR (ou)
from django.db.models import Q
# Paginação 
from django.core.paginator import Paginator


# View para criar contatos
def create(request):
    # Aquivos que são enviados para a view
    # context = { 
    #     'site_title': contact_name,
    #     'contact': single_contact,
    # }
    context = {}

    return render(
        request,
        'contact/create.html',
        context=context,
    )   