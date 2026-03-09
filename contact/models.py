from django.db import models
# Usada para criar uma data automaticamente
from django.utils import timezone


# id (primary key - automático) - campo primordial
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key - chave estrangeria), show (boolean), 
# owner (foreign key), picture (imagem)

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

Obs.: Atribuir blank = True torna o campo opcional.
Obs.2: Qualquer alteração no model, é necessário fazer ambos
os códigos do migrate, que estão em commands.txt.
Obs.3: É necessário registrar os models no arquivo admin.py.
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


    # Defini como o contato será salvo no admin
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}' 
