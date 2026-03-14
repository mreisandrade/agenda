from django.db import models
# Usada para criar uma data automaticamente
from django.utils import timezone
# Model que contém os usuários
from django.contrib.auth.models import User


# id (primary key - automático) - campo primordial
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key - chave estrangeria), show (boolean), 
# picture (imagem)

# Por último, pois já é nativo do Django
# owner (foreign key)

# Create your models here.

''' Campos dos models (tabelas)
    - CharFiedl: campo de texto, recebe o comprimento máximo
    (max_length) da string; geralmente, são limitadas até 255 
    caracteres
    - EmailField: campo de email, recebe o comprimento máximo
    (max_length) do email
    - DateTimeField: campo de data e hora
    - DateField: campo apenas de data
    - TextField: campo de texto, porém com tamanhos maiores;
    não é necessário passar o tamanho máximo
    - BooleanFiel: campo para valores booleanos. Pode receber
    o valor padrão em "default"
    - ImageField: campo de imagem. Recebe como parâmentro
    upload_to, que é para onde os arquivos enviados serão
    armazenados. É necessário instalar o pillow para criar
    campos de imagens. Além disso, é necessário configurar
    o arquivo urls.py do projeto para poder acessar a imagem.
    - ForeignKey: campo de chave estrangeira, que são chaves 
    que apontam para outros banco de dados (neste caso, 
    models). São utilizadas para padronizar entrada de dados.
    Recebe obrigatoriamente o model estrangeiro e o on_delete,
    que significa o que será feito quando a chave estrangeira
    é apagada. Os dados associados a foreign key são conectados
    pela primary key, ou seja, sua informações (exceto id),
    podem ser alteradas, alterando também todos os dados que
    estão associados a essa chave.
        + models.CASCADE: deleta todos os dados assossiados a
        categoria
        + models.SET_NULL: configura os dados assossiados a
        categoria como nulos
    
Obs.: Atribuir blank = True torna o campo opcional.
Obs.2: Qualquer alteração no model, é necessário fazer ambos
os códigos do migrate, que estão em commands.txt.
Obs.3: É necessário registrar os models no arquivo admin.py.
Obs.4: Normalmente, imagens não são guardadas em bancos de 
dados por questão de performance. Assim, são guardados os 
links que apontam para as imagens.
'''

# Usada como foreign key da base Contact
class Category(models.Model):
    # Corrindo o problema do plural
    # Antes, estava aparecendo Categorys
    # A classe Meta é usada para configurar parâmetros do model
    class Meta:
        # Nome no singular
        # _(): quer dizer tradução, no Django
        verbose_name = 'Category'
        # Nome no plural
        verbose_name_plural = 'Categories'


    name = models.CharField(max_length=50)


    # Importante ter em todos os models
    def __str__(self) -> str:
        return f'{self.name}' 


''' User do Django
    - Por padrão, o Django já vem com um model de usuários (users)
    - Pode ser acessada por
        from django.contrib.auth.models import User
    - O ideal não é alterar diretamente esse model, caso seja
    necessário criar mais campos para o usuário, e sim extender
    a base criando outro model.
    - Para criar um usuário, insira o comando
        user = User.objects.create_user(
            username='usuario',
            password='123',
        )
    - O create_user é lease, ou seja, não precisa do save() pois
    o usuário é salvo automaticamente.
    - Para permitir que o usuário acesse a área admin, insira
    os comando abaixo. Mesmo com o staff ativo, é necessário
    inserir as permissões para que esse usuário faça modificações
    dentro da área administrativa. 
        user.is_staff = True
        user.save()
    - Para deletar o usuário, 
        user.delete()
'''

# O nome da classe do model é criada no singular
class Contact(models.Model):
    # Inserir os nomes dos campos
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # Atribuir blank = True torna o campo opcional
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    # Atribuir blank = True torna o campo opcional
    description = models.TextField(blank=True)
    # Exibe ou não o contato
    # default: valor padrão
    show = models.BooleanField(default=True)
    # upload_to: para onde as imagens serão enviadas
    # Cria uma pasta chamada de ano e outra chamada de mês
    # para deixar a pasta mais organizada
    picture = models.ImageField(
        blank=True, 
        upload_to='pictures/%Y/%m/',
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True,
        # Permite que o valor seja nulo
        null=True,
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        # Permite que o valor seja nulo
        null=True,
    )

    # Defini como o contato será salvo no admin
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}' 
