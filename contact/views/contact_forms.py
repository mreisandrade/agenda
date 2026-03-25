from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# Exige que o usuário esteja logado para acesasr a view
from django.contrib.auth.decorators import login_required

# Importando o formulário criado 
from contact.forms import ContactForm
from contact.models import Contact


# Exige que o usuário esteja logado para acesasr a view
# Caso não esteja, redireciona para login_url
@login_required(login_url='contact:login')
# View para criar contatos
def create(request):
    # Criando uma variável reversa
    # É usada no HTML para ser usada dinamicamente
    form_action = reverse('contact:create')

    # Verifica se o request foi POST
    # Reenvia os dados para a página (mantém os dados)
    if request.method == 'POST':
        # Passando o formulário para o html
        # Todo lugar com POST também deve receber FILES
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            # Passando a variável reversa para a página
            'form_action': form_action,
        }

        # Verifica se o form é válido
        # Verifica todas as validações, incluse as criadas
        if form.is_valid():
            # Salva o formulário na base de dados
            # form.save()
            
            # Não salva o dado imediatamente
            contact = form.save(commit=False)
            # Mudando outros atributos do contato
            # contact.show = False

            # Atribuindo o contato ao proprietário
            # (usuário logado)
            # Isso é garantido pelo @login_required
            contact.owner = request.user

            # Salva o formulário na base de dados
            form.save()

            # Redirecionando a página contact:create
            # Envia o id do contato para a view
            return redirect('contact:update', contact_id=contact.id)


        return render(
            request,
            'contact/create.html',
            context=context,
        )   

    # Passando o formulário para o html
    context = {
        'form': ContactForm(),
        # Passando a variável reversa para a página
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context=context,
    ) 
  

# Exige que o usuário esteja logado para acesasr a view
# Caso não esteja, redireciona para login_url
@login_required(login_url='contact:login')
# View para atualizar um contato
def update(request, contact_id):
    # Obtém o contato
    contact = get_object_or_404(
        Contact, 
        id=contact_id,
        show=True,
        # Verifica se o usuário logado é o proprietário
        owner=request.user,
    )

    # Criando uma variável reversa
    # É usada no HTML para ser usada dinamicamente
    form_action = reverse('contact:update', args=(contact_id,))

    # Verifica se o request foi POST
    # Reenvia os dados para a página (mantém os dados)
    if request.method == 'POST':
        # Passando o formulário para o html com as informações
        # do contato que será atualizado
        # Todo lugar com POST também deve receber FILES
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            # Passando a variável reversa para a página
            'form_action': form_action,
        }

        # Verifica se o form é válido
        # Verifica todas as validações, incluse as criadas
        if form.is_valid():
            # Salva o formulário na base de dados
            # form.save()
            
            # Não salva o dado imediatamente
            contact_form = form.save(commit=False)
            # Mudando outros atributos do contato
            # contact.show = False

            # Salva o formulário na base de dados
            form.save()

            # Redirecionando a página contact:create
            # Envia o id do contato para a view
            return redirect('contact:update', contact_id=contact_form.id)


        return render(
            request,
            'contact/create.html',
            context=context,
        )   

    # Passando o formulário para o html
    context = {
        'form': ContactForm(instance=contact),
        # Passando a variável reversa para a página
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context=context,
    ) 


# Exige que o usuário esteja logado para acesasr a view
# Caso não esteja, redireciona para login_url
@login_required(login_url='contact:login')
# View para deletar um contato
def delete(request, contact_id):
    # Obtém o contato
    contact = get_object_or_404(
        Contact, 
        id=contact_id,
        show=True,
    )

    # Criando uma confirmação
    # Deve existir um input chamado confirmation
    # Se não existir, seja no
    confirmation = request.POST.get('confirmation', 'no')
    print(confirmation)

    if confirmation == 'yes':
        # Deleta o contato
        contact.delete()
        # Redireciona para a página principal
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
