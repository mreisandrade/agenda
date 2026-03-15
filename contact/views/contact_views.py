from django.shortcuts import render, get_object_or_404
# Importando o model dos contatos (database)
from contact.models import Contact
# Usado para levar a exceção de página não encontrada (Erro 404)
from django.http import Http404


# Create your views here.
def index(request):
    # Coletando os dados dos contatos
    # Ordenando por ordem decrescente de id
    # contacts = Contact.objects.all().order_by('-id')

    # Coletando os dados dos contatos que devem ser mostrados
    # Ordenando por ordem decrescente de id
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    # Pode-se usar fatiamento nos dados
    # Ex.: contacts = Contact.objects.filter(show=True)[0:10]

    # Vizualizando qual consulta está sendo realizada
    # print(contacts.query)

    # Aquivos que são enviados para a view
    context = { 
        'site_title': 'Contatos',
        'contacts': contacts,
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
