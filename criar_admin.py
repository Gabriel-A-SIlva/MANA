# criar_admin.py

import os
import django

# Substitua 'MANA' pelo nome da pasta do seu projeto onde está o settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from admin.models.admin import Admin  # Altere 'paineladmin' para o nome do seu app
from django.contrib.auth.hashers import make_password

Admin.objects.create(
    nome='root',
    senha_acesso=make_password('123456')
)

print("Admin criado com sucesso!")
