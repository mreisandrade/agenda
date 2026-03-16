from django.shortcuts import render, get_object_or_404, redirect
# Importando o model dos contatos (database)
from contact.models import Contact
# Usado para levar a exceção de página não encontrada (Erro 404)
from django.http import Http404
# Classe para usar condições OR (ou)
from django.db.models import Q
# Paginação 
from django.core.paginator import Paginator


# Create your views here.
# Página principal dos contatos
def index(request):
    # Coletando os dados dos contatos
    # Ordenando por ordem decrescente de id
    # contacts = Contact.objects.all().order_by('-id')

    # Coletando os dados dos contatos que devem ser mostrados
    # Ordenando por ordem decrescente de id
    contacts = Contact.objects.filter(show=True).order_by('-id')

    # Paginação
    # 10: número máximo de itens por página
    paginator = Paginator(contacts, 10)
    # Criando os objetos da página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pode-se usar fatiamento nos dados
    # Ex.: contacts = Contact.objects.filter(show=True)[0:10]

    # Vizualizando qual consulta está sendo realizada
    # print(contacts.query)

    # Aquivos que são enviados para a view
    context = { 
        'site_title': 'Contatos',
        # 'contacts': contacts, # antes da paginação
        'page_obj': page_obj, # depois da paginação
    }

    return render(
        request,
        'contact/index.html',
        context=context,
    )


# Contatos filtrados pela barra de pesquisa
def search(request):
    # Valores enviados pelo form
    # search_value = request.GET
    # Tenta obter a chave q. Caso não ache, retorna ''
    search_value = request.GET.get('q', '')
    search_value = search_value.strip()

    # Caso não seja encontrado nada, redireciona para o index
    if not search_value:
        return redirect('contact:index')
    
    # Forma de buscar dados
    # Para adicionar o lookup, coloque o nome do campo, seguido
    #  (__ - dunder score) e informe o lookup desejado
    # exact: case sensitite - é exatamente igual
    # iexact: case insensitite - é exatamente igual
    # contains: case insensitite - contém esse dado
    # contains: case sensitite - contém esse dado
    # in: está em um iterável
    # e outros (ver link)
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups

    contacts = Contact.objects \
    .filter(show=True) \
    .filter(
        # O que permite fazer a operação OR (ou)
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
    ) \
    .order_by('-id')

    # Paginação
    # 10: número máximo de itens por página
    paginator = Paginator(contacts, 10)
    # Criando os objetos da página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Nesse caso, foi necessário mudar todos os links para
    # incluir a variável q, pois o paginator muda isso

    # Aquivos que são enviados para a view
    context = { 
        'site_title': 'Search',
        # 'contacts': contacts, # antes da paginação
        'page_obj': page_obj, # depois da paginação
        # Enviando a variável para matenter o valor da pesquisa
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context=context,
    )


# Create your views here.
def contact(request, contact_id):
    # O contact_id é enviado pela URL
    # Coletando os dados do contato
    # single_contact = Contact.objects.get(pk=contact_id)

    '''
        Da forma anterior, ao solicitar o contato de um id que
        não existe, ocorrerá um erro por causa do get. Para 
        evitar isso, foi usado um filter(). Como o filter 
        retorna vários valores (QuerySet), foi usado o first()
        para coletar apenas o primeiro dado.
    '''
    # single_contact = Contact.objects.filter(pk=contact_id).first(   )

    # Caso o contato não seja encontrado, mostra o erro 404
    # if single_contact is None:
    #     raise Http404

    # Para fazer isso de forma mais direta, tem-se o atalho que
    # ou obtém o objeto ou levando o erro 404
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    # Outras formas de fazer isos é passando o manager
    # single_contact = get_object_or_404(
    #     Contact.objects,
    #     # Nesse caso, é AND (as duas codições devem ser verdadeiras)
    #     pk=contact_id,
    #     show=True,
    # )
    # Ou passando a consulta direto
    # single_contact = get_object_or_404(
    #     # Nesse caso, é AND (as duas codições devem ser verdadeiras)
    #     Contact.objects.filter(pk=contact_id, show=True),
    # )

    contact_name = f'{single_contact.first_name} {single_contact.last_name}'

    # Aquivos que são enviados para a view
    context = { 
        'site_title': contact_name,
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context=context,
    )   
