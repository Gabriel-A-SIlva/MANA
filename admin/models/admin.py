from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Admin(models.Model):
    nome = models.CharField(max_length=255)
    senha_acesso = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Criptografa apenas se a senha não estiver criptografada
        if not self.senha_acesso.startswith('pbkdf2_'):
            self.senha_acesso = make_password(self.senha_acesso)
        super().save(*args, **kwargs)

    def verificar_senha(self, senha_digitada):
        return check_password(senha_digitada, self.senha_acesso)
