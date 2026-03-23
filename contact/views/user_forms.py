from django.shortcuts import render, redirect
# Usado para enviar flash messages
from django.contrib import messages

from contact.forms import RegisterForm


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
            return redirect('contact:index') 
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )
