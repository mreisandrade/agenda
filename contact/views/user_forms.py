from django.shortcuts import render, redirect
# Usado para enviar flash messages
from django.contrib import messages, auth
# Formulário do form do autenticador
from django.contrib.auth.forms import AuthenticationForm
# Exige que o usuário esteja logado para acesasr a view
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, RegisterUpdateForm


''' Flash messages
    - Enviar mensagems para a view
    - A mensagem pode ser enviada de qualquer lugar
    - Só vai deixar de existir quando for exibida em algum
    template qualquer
    - Tipo:
        + warning: alerta
        + sucess: sucesso
        + info: informação
        + error: erro 
    - Uma mensagem precisa ser capturada em algum lugar
'''


def register(request):
    form = RegisterForm()

    # Mensagem registrada
    # messages.info(request, 'Um texto qualquer')
    # messages.success(request, 'Um texto qualquer')
    # messages.warning(request, 'Um texto qualquer')
    # messages.error(request, 'Um texto qualquer')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login') 
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )


# View de login
def login_view(request):
    # Formulário padrão de autenticador de usuário do Django
    # O primeiro parâmetro é a request
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        # Verifica se o formulário é válido 
        # (usuário logado com sucesso)
        if form.is_valid():
            # Pega o usuário logado
            # Se nenhum estiver logado, vai aparecer Anonymous User
            user = form.get_user()
            # Fazendo o login do usuário
            auth.login(request, user)
            # Exibindo uma mensagem de sucesso
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        else:
            messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        }
    )


# Exige que o usuário esteja logado para acesasr a view
# Caso não esteja, redireciona para login_url
@login_required(login_url='contact:login')
# View de logout
def logout_view(request):
    # Fazendo o logout do usuário
    auth.logout(request)
    return redirect('contact:login')


# Exige que o usuário esteja logado para acesasr a view
# Caso não esteja, redireciona para login_url
@login_required(login_url='contact:login')
def user_update(request):
    # Passando os dados do usuário LOGADO para o formulário
    form = RegisterUpdateForm(instance=request.user)

    # Se o método naõ for POST (for GET)
    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form,
            }
        )
    
    # Pegando os dados do formulário
    form = RegisterUpdateForm(
        instance=request.user,
        data=request.POST,
    )

    # Caso o formulário não for válido
    if not form.is_valid():
        # Renderiza a mesma view de atualização dos dados
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form,
            }
        )

    # Caso seja válido, atualiza os dados
    # user vem do formulário RegisterUpdateForm
    user = form.save()

    # Renderiza a mesma view de atualização dos dados
    return redirect('contact:user_update')
