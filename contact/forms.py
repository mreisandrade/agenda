# Usado para formulários no Django
from django import forms
# Para validação de dados
from django.core.exceptions import ValidationError
# Importando o model
from contact.views import Contact


# Criando um formulário com base em um modelo (ModelForm)
class ContactForm(forms.ModelForm):
    # Outra forma de mudar os widgets e outras características
    # Recriando o campo
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # Atriibutos da tag
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva aqui',
            },
        ),
        label='Primeiro nome',
        # Texto de ajuda
        # Necessário adicionar no HTML
        help_text='Texto de ajuda para seu usuário',
    )

    # Adicionando outro campo que não foi criado no model
    # qualquer = forms.CharField(
    #     widget=forms.TextInput(),
    # )


    # Configurações do form
    class Meta:
        # Em qual model é baseado o form
        model = Contact
        # Campos do formulário
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
        ]
        # Configurando o widgets dos campos
        # forms.PasswordInput()
        # forms.Textarea()
        # forms.TextInput()
        # Ver link: https://docs.djangoproject.com/en/6.0/ref/forms/widgets/
        # widgets = {
        #     # Configura como campo de texto
        #     'first_name': forms.TextInput(
        #         # Atributos do widgets
        #         attrs={
        #             # Atriibutos da tag
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         },
        #     ),
        # }


    # Método chamado antes de salvar os dados na base
    # Caso ocorra algum erro, não salva na base de dados
    # Tem acesso a todos os campos do formulário
    def clean(self):
        # Dados limpos do formulário
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            # Classe do erro
            msg = ValidationError(
                # Mensagem do erro
                'Primeiro nome não pode ser igual ao segundo',
                # Código do erro
                # Pode ser usado pelo programador para fazer
                # alguma lógica
                code='invalid',
            )
            # Adiciona um erro
            self.add_error(
                # Campo monitorado
                'first_name',
                # Classe do erro
                msg,
            )
            # Adiciona um erro
            self.add_error(
                # Campo monitorado
                'last_name',
                # Classe do erro
                msg,
            )

        # Erros que não estão atrelados à campos
        # Adiciona um erro
            self.add_error(
                # Campo monitorado
                None,
                # Classe do erro
                ValidationError(
                    # Mensagem do erro
                    'Mensagem de erro',
                    # Código do erro
                    # Pode ser usado pelo programador para fazer
                    # alguma lógica
                    code='invalid',
                ),
            )

        # No clean, é necessário retornar o super do clean
        return super().clean()
    

    # Método que valida a entrada do campo first_name
    # O nome do método é SEMPRE clean_<nome_do_campo>
    # Deve retornar o valor do campo 
    def clean_first_name(self):
        # Dados limpos do formulário
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                # Campo monitorado
                'first_name',
                # Classe do erro
                ValidationError(
                    # Mensagem do erro
                    'Não escreva ABC neste campo',
                    # Código do erro
                    # Pode ser usado pelo programador para fazer
                    # alguma lógica
                    code='invalid',
                ),
            )

        return first_name
