from admin.models.saladas import Salada
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
import json

def create_saladas(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_salada')
        if not nome:
            messages.success(request, 'Nome não pode ser vazio.')
    if Salada.objects.filter(nome=nome).exists():
        messages.success(request, 'salada já existe.')
    # Cria uma nova instância de salada e salva no banco de dados
    salada = Salada(nome=nome)
    salada.save()
    messages.success(request, 'Cadastro realizado com sucesso.')
    return redirect('index_admin')

def read_saladas(request):
    saladas = Salada.objects.all().values()
    print(saladas)
    return JsonResponse(list(saladas), safe=False)


def update_saladas(request, salada_id):
    salada = Salada.objects.get(id=salada_id)
    if request.method == 'PUT':
        body = json.loads(request.body)
        nome = body.get('nome')
        salada.nome = nome
        salada.save()
        return JsonResponse({'success': True, 'message': 'Proteína atualizada com sucesso!'})
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

def delete_saladas(request, salada_id):
    salada = Salada.objects.get(id=salada_id)
    if request.method == 'DELETE':
        salada.delete()
        return JsonResponse({'success': True, 'message': 'Proteína deletada com sucesso!'})
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)
