''' Pacote views

    - O __init__ é o primeiro arquivo a ser executado quando
    o pacote é importado
    - Esse pacote foi criado para organizar melhor as views
    - Equivalente ao views.py padrão do Django (foi excluído
    para evitar conflito com o pacote atual)
    - Toda vez que for adicionado um novo arquivo no pacote 
    views, é necessário importá-lo aqui
'''
from .contact_views import *
from .contact_forms import *
