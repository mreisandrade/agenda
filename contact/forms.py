# Usado para formulários no Django
from django import forms
# Para validação de dados
from django.core.exceptions import ValidationError
# Importando o model dos contatos
from contact.views import Contact
# Importando o model do usuários
from django.contrib.auth.models import User
# Importando o formulário para criação de usuários
from django.contrib.auth.forms import UserCreationForm
# Validador de senhas
from django.contrib.auth import password_validation


# Criando um formulário com base em um modelo (ModelForm)
class ContactForm(forms.ModelForm):
    # Outra forma de mudar os widgets e outras características
    # Recriando o campo
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             # Atriibutos da tag
    #             'class': 'classe-a classe-b',
    #             'placeholder': 'Escreva aqui',
    #         },
    #     ),
    #     label='Primeiro nome',
    #     # Texto de ajuda
    #     # Necessário adicionar no HTML
    #     help_text='Texto de ajuda para seu usuário',
    # )

    # Adicionando outro campo que não foi criado no model
    # qualquer = forms.CharField(
    #     widget=forms.TextInput(),
    # )

    # Alterando o campo da picture
    # Normalmente, a imagem não é apagada do servidor
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                # Aceita qualquer imagem
                'accept': 'image/*'
            },
        ),
    )


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
            'picture',
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


# Formulário para a criação de usuários
class RegisterForm(UserCreationForm):
    # Alterando os campos
    first_name = forms.CharField(
        # Obriga o envio 
        required=True,
        # Tamanho mínimo requerido
        # min_length=3,
        # Mundando as mensagens de erro
        # error_messages={
        #     'required': 'Tem que enviar o nome, pow',
        # }
    )
    last_name = forms.CharField(
        # Obriga o envio 
        required=True,
    )
    email = forms.EmailField(
        # Obriga o envio 
        required=True,
    )

    # A partir do momento em que a classe Meta é criada, é
    # necessário informar os campos do formulário
    class Meta:
        # model utilizado
        model = User
        # Campos do formulário
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            # Confirmação da senha
            'password2',
        ]

    
    # Valida o e-mail
    def clean_email(self):
        # Obtendo o e=mail do usuário
        email = self.cleaned_data.get('email')

        # Verificando se o email já está cadastrado
        if User.objects.filter(email=email).exists():
            # Exibe um erro caso já exista o email
            self.add_error(
                'email',
                ValidationError(
                    'Já existe esse e-mail',
                    code='invalid',
                ),
            )

        return email
    

# Formulário para atualizar dados do usuário
class RegisterUpdateForm(forms.ModelForm):
    # Alterando campos do formulário
    first_name = forms.CharField(
        # Obriga o envio 
        required=True,
        # Tamanho mínimo requerido
        min_length=3,
        # Tamanho máximo requerido
        max_length=30,
        # Mensagem de ajuda
        help_text='Necessário',
    )
    last_name = forms.CharField(
        # Obriga o envio 
        required=True,
        # Tamanho mínimo requerido
        min_length=3,
        # Tamanho máximo requerido
        max_length=30,
        # Mensagem de ajuda
        help_text='Necessário',
    )
    # Senhas (normal + confirmação)
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
            },
        ),
        # Exibe os requisitos da senha
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
            },
        ),
        help_text='Use the same password as before',
        required=False,
    )


    # A partir do momento em que a classe Meta é criada, é
    # necessário informar os campos do formulário
    class Meta:
        # model utilizado
        model = User
        # Campos do formulário
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]


    # Validando os dados enviados pelo usuário
    def clean(self):
        # As senhas não são salvas automaticamente pois
        # necessitam ser criptografadas
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Verifica se há dados no password1
        if password1 or password2:
            # Verifica se as senhas são diferentes
            if password1 != password2:
                # Verifica se as senhas são diferentes
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem.')
                )

        return super().clean()
    

    # Função que salva os dados (inclusive a senha)
    def save(self, commit=True):
        # Pegando os dados enviados
        cleaned_data = self.cleaned_data
        # Pegando o usuário sem comitar as informações
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        # Configurando a nova senha
        if password:
            user.set_password(password)

        # Salvando os dados
        if commit:
            user.save()

        # É necessário retornar o usuário 
        # Para ser usado na view
        return user


    # Valida o e-mail
    def clean_email(self):
        # Obtendo o e=mail do usuário
        email = self.cleaned_data.get('email')
        # Email atual do usuário logado 
        current_email = self.instance.email

        # Verifica se o email é diferente do cadastro do usuário
        # Se for, é porque ele quer alterar o email
        if current_email != email:
            # Verificando se o email já está cadastrado
            if User.objects.filter(email=email).exists():
                # Exibe um erro caso já exista o email
                self.add_error(
                    'email',
                    ValidationError(
                        'Já existe esse e-mail',
                        code='invalid',
                    ),
                )

        return email


    # Valida a senha
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # Se houver password (quer modificar a senha)
        if password1:
            # Valida a senha
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                # Mostrando os erros ao usuário
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1
        