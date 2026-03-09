from django.contrib import admin
# Model criado no app Contact
from contact import models


# Register your models here.
# Criando a conexão do model Contact criado no app Contact
# Por padrão, o nome da classe é definido como 
#   NomeDoApp + Admin: NomeDoAppAdmin
# Para configurar o model, normalmente, usa-se o decorator 
# abaixo. Recebe como parâmentro o model criado.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ...