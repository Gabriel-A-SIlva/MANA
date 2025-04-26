from admin.models.proteinas import Proteina
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
import json
def create_proteinas(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_proteina')
        if not nome:
            messages.success(request, 'Nome não pode ser vazio.')
    if Proteina.objects.filter(nome=nome).exists():
        messages.success(request, 'Proteina já existe.')
    # Cria uma nova instância de Proteina e salva no banco de dados
    proteina = Proteina(nome=nome)
    proteina.save()
    messages.success(request, 'Cadastro realizado com sucesso.')
    return redirect('index_admin')

def read_proteinas(request):
    proteinas = Proteina.objects.all().values()
    print(proteinas)
    return JsonResponse(list(proteinas), safe=False)


def update_proteinas(request, proteina_id):
    proteina = Proteina.objects.get(id=proteina_id)
    if request.method == 'PUT':
        body = json.loads(request.body)
        nome = body.get('nome')
        proteina.nome = nome
        proteina.save()
        return JsonResponse({'success': True, 'message': 'Proteína atualizada com sucesso!'})
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

def delete_proteinas(request, proteina_id):
    proteina = Proteina.objects.get(id=proteina_id)
    if request.method == 'DELETE':
        proteina.delete()
        return JsonResponse({'success': True, 'message': 'Proteína deletada com sucesso!'})
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)
