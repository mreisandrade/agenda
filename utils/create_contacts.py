import os
import sys
from datetime import date
from pathlib import Path
from random import choice

import django
# Importa as variáveis do settings.py da pasta project
from django.conf import settings


# Vai para a pasta raíz do projeto
DJANGO_BASE_DIR = Path(__file__).parent.parent
# Quantidade de contatos gerados
NUMBER_OF_OBJECTS = 1000

# Inclui a pasta raíz do projeto nos caminhos do python
sys.path.append(str(DJANGO_BASE_DIR))

# Faz configurações que são realizadas dentro do manage.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False
django.setup()


if __name__ == '__main__':
    # Essas importações estão feitas dentro do if __name__ == '__main__'
    # apenas para enviar erro de importações, pois o Python tende
    # reordenas os imports

    # Biblioteca utilizada para gerar dados falsos (para testes)
    import faker

    from contact.models import Category, Contact

    # Deleta todos os contatos e categorias
    Contact.objects.all().delete()
    Category.objects.all().delete()

    # Configura o Faker para vir com nomes brasileiros
    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    # Gerando as categorias (sem salvar)
    django_categories = [Category(name=name) for name in categories]

    # Salvando as categorias na base de dados
    for category in django_categories:
        category.save()

    django_contacts = []

    # Itera sobre o número de contatos solicitados
    for _ in range(NUMBER_OF_OBJECTS):
        # Pega um perfil falso do Faker
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: date = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            # Cria um contato (sem salvar)
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        # Salva vários objetos ao mesmo tempo
        Contact.objects.bulk_create(django_contacts)
