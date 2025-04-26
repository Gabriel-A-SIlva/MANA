from admin.models.arrozes import Arroz
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
import json

def create_arrozes(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_arroz')
        if not nome:
            messages.success(request, 'Nome não pode ser vazio.')
    if Arroz.objects.filter(nome=nome).exists():
        messages.success(request, 'arroz já existe.')
    # Cria uma nova instância de arroz e salva no banco de dados
    arroz = Arroz(nome=nome)
    arroz.save()
    messages.success(request, 'Cadastro realizado com sucesso.')
    return redirect('index_admin')

def read_arrozes(request):
    arrozes = Arroz.objects.all().values()
    print(arrozes)
    return JsonResponse(list(arrozes), safe=False)


def update_arrozes(request, arroz_id):
    arroz = Arroz.objects.get(id=arroz_id)
    if request.method == 'PUT':
        body = json.loads(request.body)
        nome = body.get('nome')
        arroz.nome = nome
        arroz.save()
        return JsonResponse({'success': True, 'message': 'Proteína atualizada com sucesso!'})
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

def delete_arrozes(request, arroz_id):
    arroz = Arroz.objects.get(id=arroz_id)
    if request.method == 'DELETE':
        arroz.delete()
        return JsonResponse({'success': True, 'message': 'Proteína deletada com sucesso!'})
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)
