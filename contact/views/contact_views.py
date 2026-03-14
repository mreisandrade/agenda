from django.shortcuts import render
# Importando o model dos contatos (database)
from contact.models import Contact


# Create your views here.
def index(request):
    # Coletando os dados dos contatos
    contacts = Contact.objects.all()

    # Aquivos que são enviados para a view
    context = { 
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context=context,
    )   
