from django.shortcuts import render
from CarteiraApp.models import Vendas,Cliente
from datetime import datetime
from django.db.models import Prefetch

# Após o request atraves do protocolo HTTP, renderiza nossa tela inicial.
def homepage(request):
    return render(request,'homepage.html')

# Após a requisição de filtro por parte do Cliente, retornar o resultado esperado.
def dash_vendas(request):
  # Aqui inicio o dicionario 'data' e declaro as variaveis para o filtro, todos os campos vieram do front-end.
    data = {}
    start_date = request.GET.get('start_date') # Campo de data inicial
    end_date = request.GET.get('end_date')# Campo de data final
    loja = request.GET.get('loja_field')# Campo de loja
    cliente_field = request.GET.get('cliente_field')# Campo de cliente
    pg = request.GET.get('pg_field')# Campo de metódo de pagamento
    sexo = request.GET.get('sexo_field')# Campo de sexo do público-alvo
    forn = request.GET.get('forn_field')# Campo de fornecedor
    promo = request.GET.get('promo_field')# Campo de promoção
    if start_date and end_date:# Inicio da condição
      inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
      fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
      data['vendas'] = Vendas.objects.filter(data_vnd__range=[inidt_date, fimdt_date])
    elif sexo == 'Masculino' or sexo == 'Feminino':
      data['vendas'] = Vendas.objects.all().filter(cod_cliente__sexo_cliente=sexo)
    else:
      data['vendas'] = Vendas.objects.all()
    return render(request,'dashboard_vendas.html', data)