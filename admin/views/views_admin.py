from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from admin.models.admin import Admin

def index_admin(request):
    return render(request, 'index.html')

def sign_in_admin(request):
    if request.user.is_authenticated:
        return redirect('index_admin')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha_acesso = request.POST.get('senha_acesso')

        # Verifica se os campos foram preenchidos
        if not nome or not senha_acesso:
            if not nome:
                messages.error(request, "O nome é obrigatório.")
            if not senha_acesso:
                messages.error(request, "A senha é obrigatória.")
            return render(request, 'sign_in.html')

        try:
            admin = Admin.objects.get(nome=nome)

            # Verifica senha criptografada
            if admin.verificar_senha(senha_acesso):
                request.session['user_id'] = admin.id
                messages.success(request, "Login realizado com sucesso!")
                return redirect('index_admin')
            else:
                messages.error(request, "Senha incorreta!")

        except Admin.DoesNotExist:
            messages.error(request, "Admin não encontrado.")
            return render(request, 'sign_in.html')

    return render(request, 'sign_in.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('sign_in_admin')