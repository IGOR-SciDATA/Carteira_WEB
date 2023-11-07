from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as log
from django.core.paginator import Paginator
from crudapp.forms import FormCliente,FormPedido,FormRecibo,FormCarro,FormURotas,FormPerfil,FormNotas,FormEmpresa
from crudapp.models import Rotas,Abastecimentos,URotas,RecibosPag,Carros,Perfil,NotasRecebimento,Empresa
from django.db.models import Sum, Min
import re
from datetime import date
from datetime import datetime
x = date.today()

# Transmite o dicionario para a Tela de Rotas (USER)
def home(request):
    data = {}
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     moto = request.user
     data['db'] = Rotas.objects.filter(user=moto, dia__range=[ini_date, fim_date])
    else:
        data['db'] = Rotas.objects.filter(user=request.user).order_by('-id')
    return render(request, 'index.html', data)

# Transmite o dicionario para a Tela de Rotas (ADM)
def rotadm(request):
    data = {}
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    idrota = request.GET.get('id_rota')
    empresa_campo = request.GET.get('rota_empresa')
    moto_campo = request.GET.get('moto_field')
    data['bd'] = User.objects.all()
    data['rotas'] = URotas.objects.all()
    data['empresas'] = Empresa.objects.all()

    if start_date and end_date and moto_campo == 'TODOS' and empresa_campo == 'TODOS':
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     #moto = request.GET.get('moto_field')
     data['db'] = Rotas.objects.filter(dia__range=[ini_date, fim_date]).order_by('-id')
    
    elif start_date and end_date and moto_campo != 'TODOS' and empresa_campo != 'TODOS':
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     #moto = request.GET.get('moto_field')
     data['db'] = Rotas.objects.filter(user=moto_campo,empresa=empresa_campo, dia__range=[ini_date, fim_date]).order_by('-id')

    elif start_date and end_date and empresa_campo != 'TODOS':
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     data['db'] = Rotas.objects.filter(empresa=empresa_campo, dia__range=[ini_date, fim_date]).order_by('-id')

    elif start_date and end_date and moto_campo != 'TODOS':
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     data['db'] = Rotas.objects.filter(user=moto_campo, dia__range=[ini_date, fim_date]).order_by('-id')


    else:
     rotas = Rotas.objects.all().order_by('-id')
     rotas_paginator = Paginator(rotas, 10)
     page_num = request.GET.get('page')
     data['db'] = rotas_paginator.get_page(page_num)
    return render(request, 'index.html', data)

def empresas(request):
   data = {}
   data['empresas'] = Empresa.objects.all()
   return render(request, 'empresas.html', data)

def update_all(request):
 if 'id_rota' in request.POST: 
    valor = request.POST.getlist('id_rota')
    stts = request.POST.get('rstatus')
    valores = [int(objeto) for objeto in valor]
 for pk in valores:    
    Rotas.objects.filter(id=pk).update(status=stts)
 return redirect('rotadm')

def pay_oil(request):
 if 'id_oil' in request.POST:
    id = request.POST.getlist('id_oil')
    data = {}
    data['ids'] = ",".join(id)
    data['form'] = FormRecibo()
    data['day'] = x.strftime('%d/%m/%Y')
    data['bd'] = User.objects.all()
 return render(request, 'cadrecibos.html', data)

def pay_rota(request):
 if 'id_rota' in request.POST:
    id = request.POST.getlist('id_rota')
    data = {}
    data['pks'] = ",".join(id)
    data['form'] = FormRecibo()
    data['day'] = x.strftime('%d/%m/%Y')
    data['bd'] = User.objects.all()
 return render(request, 'cadrecibos.html', data)

def receive_rota(request):
 if 'id_rota' in request.POST:
    id = request.POST.getlist('id_rota')
    data = {}
    data['pks'] = ",".join(id)
    data['form'] = FormRecibo()
    data['day'] = x.strftime('%d/%m/%Y')
    data['bd'] = User.objects.all()
 return render(request, 'cadrecibos.html', data)

def edit_user(request):
 data = {}
 if 'username_moto' in request.POST: 
    valor = request.POST.getlist('username_moto')
    valores = [str(objeto) for objeto in valor]
 for nome in valores:
    data['rotas'] = URotas.objects.filter(user=nome)
    data['carros'] = Carros.objects.filter(user=nome)
    data['motorista'] = User.objects.filter(username=nome)
    nomes = User.objects.filter(username=nome).values_list('username', flat=True)
    data['pk'] = "".join(map(str,nomes))
 return render(request, 'edit_user.html', data)

def edit_moto(request, pk):
   data = {}
   data['udb'] = User.objects.get(id=pk)
   return render(request, 'caduser.html', data)

# Transmite o dicionario para a Tela de Usuarios
def users(request):
   data = {}
   data['bd'] = User.objects.all()
   return render(request,'users.html', data)

# Transmite o dicionario para a Tela de Abastecimentos (ADM)
def abastecadm(request):
    data = {}
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    moto_campo = request.GET.get('moto_field')
    data['us'] = User.objects.all()
    if start_date and end_date and moto_campo == 'TODOS':
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     data['bd'] = Abastecimentos.objects.filter(dia__range=[ini_date, fim_date]).order_by('-id')
    elif start_date and end_date and moto_campo != 'TODOS':
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     data['bd'] = Abastecimentos.objects.filter(moto=moto_campo, dia__range=[ini_date, fim_date]).order_by('-id')
    else:
     data['bd'] = Abastecimentos.objects.all().order_by('-id')
    return render(request, 'abastecimento.html', data)

# Transmite o dicionario para a tela de Abastecimentos (USER) 
def abastec(request):
    data = {}
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    data['us'] = User.objects.all()
    if start_date and end_date:
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     user = request.user.username
     data['bd'] = Abastecimentos.objects.filter(moto=user, dia__range=[ini_date, fim_date])
    else:
     data['bd'] = Abastecimentos.objects.filter(moto=request.user.username)
    return render(request, 'abastecimento.html', data)

# Renderiza a tela Inicial do Sistema
def login(request):
    return render(request, 'login.html')

# Renderiza o Homepage do Usuario
def inicio(request):
    data = {}
    data['user'] = request.user
    rotas = Rotas.objects.all()
    rotas_vlr = Rotas.objects.filter(status='not').exclude(status='PAGO').values_list('receber_vlr', flat=True)
    valores = [float(sub) for sub in rotas_vlr]
    total = sum(valores)
    n = 0
    for rota in rotas:
       n += 1
    data['rotas_contadas'] = n
    data['total'] = total
    rotas_user = Rotas.objects.filter(user=request.user)
    rotas_vlr_user = Rotas.objects.filter(user=request.user).exclude(status='PAGO').values_list('vlr', flat=True)
    valores_user = [float(sub) for sub in rotas_vlr_user]
    total_user = sum(valores_user)
    data['total_user'] = total_user
    return render(request, 'homepage.html', data)

# Transmite o dicionario para a tela de Recibos
def recibospag(request):
    data = {}
    data['bd'] = User.objects.all()
    data['bn'] = RecibosPag.objects.filter(moto=request.user.username)
    search = request.GET.get('search')
    if search:
        data['db'] = RecibosPag.objects.filter(moto__icontains=search)
    else:
        data['db'] = RecibosPag.objects.all()
    return render(request, 'recibospag.html', data)

# Transmite o dicionario para o formulario de Recibos
def cad_recibo(request):
    data = {}
    data['cad'] = 'cads'
    data['form'] = FormRecibo()
    data['day'] = x.strftime('%d/%m/%Y')
    data['bd'] = User.objects.all()
    return render(request, 'cadrecibos.html', data)

# Transmite o dicionario para o formulario de Rotas
def cad_rota(request):
    data = {}
    data['form'] = FormCliente()
    data['rotas'] = URotas.objects.filter(user=request.user)
    data['modelos'] = Carros.objects.filter(user=request.user)
    data['bd'] = URotas.objects.all()
    data['day'] = x.strftime('%d/%m/%Y')
    return render(request, 'cadrota.html', data)

def cad_nf(request):
   data = {}
   data['criar'] = 'criar'
   data['form'] = FormNotas()
   data['day'] = x.strftime('%d/%m/%Y')
   data['bd'] = User.objects.all()
   return render(request,'cad_nf.html', data)

def cad_nfadm(request):
   data = {}
   data['adm'] = 'adm'
   data['form'] = FormNotas()
   data['day'] = x.strftime('%d/%m/%Y')
   data['bd'] = User.objects.all()
   return render(request,'cad_nf.html', data)

# Renderiza o formulario para Cadastros de Usuarios 
def cad_users(request):
    return render(request, 'caduser.html')

def cad_carro(request, pk):
    data = {}
    data['add'] = 'add'
    data['form'] = FormCarro()
    data['moto'] = User.objects.get(id=pk)
    data['carros'] = Carros.objects.all()
    data['bd'] = User.objects.all()
    return render(request, 'cad_carro.html', data)

def add_carro(request):
    data = {}
    data['form'] = FormCarro()
    data['criar'] = 'criar'
    return render(request, 'cad_carro.html', data)

def add_empresa(request):
    data = {}
    data['form'] = FormEmpresa()
    return render(request, 'cad_empresa.html', data)

def cad_urotas(request, pk):
   data = {}
   data['add'] = 'add'
   data['form'] = FormURotas()
   data['moto'] = User.objects.get(id=pk)
   data['empresas'] = Empresa.objects.all()
   data['rotas'] = URotas.objects.all()
   data['bd'] = User.objects.all()
   return render(request, 'cad_urotas.html', data)

def add_urotas(request):
   data = {}
   data['form'] = FormURotas()
   data['empresas'] = Empresa.objects.all()
   data['criar'] = 'esconde o campo'
   return render(request, 'cad_urotas.html', data)

# Renderiza o formulario para Cadastros de Abastecimentos
def cad_abastecimento(request):
    data = {}
    data['form'] = FormPedido()
    data['day'] = x.strftime('%d/%m/%Y')
    data['carros'] = Carros.objects.filter(user=request.user)
    return render(request, 'cadabastecimentos.html', data)

def cad_perfil(request):
    data = {}
    data['criar'] = 'criar'
    data['form'] = FormPerfil()
    data['moto'] = User.objects.get(id=request.user.id)
    data['bd'] = User.objects.all()
    return render(request, 'cad_perfil.html', data)

# Renderiza a tela para Login
def painel(request):
    return render(request, 'painel.html')

# Verifica e permite o Usuario a Logar no Sistema ou Não
def logar(request):
    user = authenticate(username=request.POST['user'], password=request.POST['pass'])
    if user is not None:
       log(request, user)
       return redirect('/inicio/')
    else:
       data = {}
       data['msg'] = 'Usuário ou Senha incorreto!'
       data['class'] = 'alert-danger'
    return render(request, 'painel.html', data)

# Desloga o Usuario do Sistema
def logouts(request):
    logout(request)
    return redirect('/')

# Verifica o request e armazena os dados do Usuario no BD
def store(request):
    data = {}
    if(request.POST['pass'] != request.POST['pass_conf']):
        data['msg'] = 'As duas senhas não conferem!'
        data['class'] = 'alert-danger'
    elif(User.objects.filter(username = request.POST['user']).exists() == True):
        data['msg'] = 'Usuário Já Cadastrado!'
        data['class'] = 'alert-danger'
        
    elif 'perm_field' in request.POST:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['pass'])
        user.first_name = request.POST['nome'] 
        user.save()
        user.user_permissions.add(21)
        perms = request.POST.get('perm_field')
        user.user_permissions.add(perms)
        data['msg'] = 'Usuário Cadastrado Com Sucesso!'
        data['class'] = 'alert-success'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['pass'])
        user.first_name = request.POST['nome'] 
        user.save()
        user.user_permissions.add(21)
        data['msg'] = 'Usuário Cadastrado Com Sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'caduser.html',data)

def update_moto(request):
    data = {}
    if(request.POST['pass'] != request.POST['pass_conf']):
        data['msg'] = 'As duas senhas não conferem!'
        data['class'] = 'alert-danger'
    else:
        pk = request.POST.get('id_moto')
        user_name = request.POST.get('user')
        user_email = request.POST.get('email')
        nome_user = request.POST.get('nome')
        User.objects.filter(id=pk).update(username=user_name, first_name=nome_user, email=user_email)
        data['msg'] = 'Usuário Atualizado Com Sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'caduser.html', data)

# Verifica o request e armazena os dados do Abastecimento no BD
def create_p(request):
  if request.method == 'POST':
    form = FormPedido(request.POST, request.FILES) 
    if form.is_valid(): 
        form = form.save(commit=False)
        form.dia = x.strftime('%d/%m/%Y')
        form.carro = request.POST.get('rcarro')
        form.moto = request.user
        form.save()
        return redirect('inicio')

def create_carro(request):
   pk = request.POST.get('motocarro')
   moto = request.POST.get('motocampo')
   Carros.objects.filter(id=pk).update(user=moto)
   return redirect('view_urotas')
      
def create_add_carro(request):
    form = FormCarro(request.POST, request.FILES)
    if form.is_valid():
     form = form.save(commit=False)
     form.save()
    return redirect('view_urotas')
      
def create_urotas(request):
   pk = request.POST.get('motorota')
   moto = request.POST.get('motocampo')
   URotas.objects.filter(id=pk).update(user=moto)
   return redirect('view_urotas')
   
def create_add_rota(request):
   form = FormURotas(request.POST or None)
   if form.is_valid():
      form = form.save(commit=False)
      form.empresa = request.POST.get('transpcampo')
      form.save()
      return redirect('view_urotas')
   
def create_perfil(request):
   form = FormPerfil(request.POST,request.FILES)
   if form.is_valid():
      form = form.save(commit=False)
      form.user = request.POST.get('motocampo')
      form.save()
      return redirect('inicio')

# Verifica o request e armazena os dados da Rota no BD    
def create(request):
    form = FormCliente(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.dia = x.strftime('%d/%m/%Y')
        form.status = 'not'
    if 'nome_rota' and 'rcarro' in request.POST: 
        valor = request.POST.getlist('nome_rota')
        number = [float(sub.split('/')[0]) for sub in valor]
        lista = [str(sub.split('/')[1]) for sub in valor]
        empresas = [str(sub.split('/')[2]) for sub in valor]
        valor_areceber = [float(sub.split('/')[3]) for sub in valor]
        carros = request.POST.getlist('rcarro')
        total = sum(number)
        form.vlr = total
        total_receber = sum(valor_areceber)
        form.receber_vlr = total_receber
        form.serv = ("," . join(lista))
        form.carro = ("," . join(carros))
        form.empresa = ("," . join(empresas))
        form.save()
        return redirect('home')

# Verifica o request e armazena os dados do Recibo no BD
def create_r(request):
    form = FormRecibo(request.POST, request.FILES)
    if 'rids' in request.POST:
        valor = request.POST.getlist('rids')
        ids_join = ''.join(valor)
        ids = ids_join.split(',')
        valores = [int(objeto) for objeto in ids]
    for pk in ids:   
        Abastecimentos.objects.filter(id=pk).update(status='PAGO')
   
    if form.is_valid():    
        form = form.save(commit=False)
        form.moto = request.POST.get('motofield')
        form.dia = request.POST.get('rday')
        form.desc_pag = request.POST.get('rdesc')
        form.status = request.POST.get('stts')
        form.tipo = request.POST.get('rtipo')
        form.save()
        return redirect('recibospag')
    
def create_rcb(request):
    form = FormRecibo(request.POST, request.FILES)

    if form.is_valid():    
        form = form.save(commit=False)
        form.moto = request.POST.get('motofield')
        form.dia = request.POST.get('rday')
        form.desc_pag = request.POST.get('rdesc')
        form.status = request.POST.get('stts')
        form.tipo = request.POST.get('rtipo')
        form.save()
        return redirect('recibospag')
    
def create_empresa(request):
   form = FormEmpresa(request.POST or None)

   if form.is_valid():
      form = form.save(commit=False)
      form.save()
      return redirect('inicio')
    
def create_rw(request):
    form = FormRecibo(request.POST, request.FILES)
    if 'rotaids' in request.POST:
        valor = request.POST.getlist('rotaids')
        ids_join = ''.join(valor)
        ids = ids_join.split(',')
        valores = [int(objeto) for objeto in ids]
        stts = request.POST.get('stts')
    for pk in ids:   
        Rotas.objects.filter(id=pk).update(status=stts)
   
    if form.is_valid():    
        form = form.save(commit=False)
        form.moto = request.POST.get('motofield')
        form.dia = request.POST.get('rday')
        form.desc_pag = request.POST.get('rdesc')
        form.status = request.POST.get('stts')
        form.tipo = request.POST.get('rtipo')
        form.save()
        return redirect('recibospag')
    
def create_nf(request):
   form = FormNotas(request.POST, request.FILES)
   if form.is_valid():
      form = form.save(commit=False)
      form.data = x.strftime('%d/%m/%Y')
      form.moto = request.user
      form.save()
      return redirect('inicio')

    
def create_nfadm(request):
   form = FormNotas(request.POST, request.FILES)
   if form.is_valid():
      form = form.save(commit=False)
      form.data = x.strftime('%d/%m/%Y')
      form.moto = request.POST.get('motocampo')
      form.save()
      return redirect('inicio')


# Passa o dicionario DB para o View dos Recibos
def viewrec(request,pk):
    data = {}
    data['rec'] = RecibosPag.objects.get(pk=pk)
    return render(request, 'view.html', data)

def view_nf(request):
    data = {}
    data['us'] = User.objects.all()
    data['nfs'] = NotasRecebimento.objects.all() # Notas mostradas para o gestor 
    data['notas'] = NotasRecebimento.objects.filter(moto=request.user.username) # Notas mostradas para os motoristas
    return render(request, 'view_nf.html', data)

def view_urotas(request):
   data = {}
   data['rotas'] = URotas.objects.all()
   data['carros'] = Carros.objects.all()
   return render(request,'view_urotas.html', data)

def meu_perfil(request):
   data = {}
   data['dados'] = Perfil.objects.get(user=request.user.id)
   data['db'] = Perfil.objects.get(user=request.user.id)
   return render(request, 'perfil.html', data)

def view_motorista(request, pk):
   data = {}
   data['back'] = 'back'
   data['dados'] = Perfil.objects.get(user=pk)
   data['db'] = Perfil.objects.get(user=pk)
   return render(request, 'perfil.html', data)

# Transmite o dicionario para a Tela de Recibos (USER)
def view_cp(request):
    data = {}
    username = request.user.username
    search1 = request.GET.get('search1')
    if search1:
     data['db'] = RecibosPag.objects.filter(moto=username,dia__icontains=search1)
    else:
     data['db'] = RecibosPag.objects.filter(moto=username)
    return render(request, 'recibosmoto.html', data)

def viewmoto(request, nome_user):
   data = {}
   data['modelos'] = Carros.objects.filter(user=nome_user)
   data['nomes'] = Carros.objects.filter(user=nome_user).values_list('nome', flat=True)
   data['rotas'] = URotas.objects.filter(user=nome_user).values_list('nome', flat=True)
   data['valores'] = URotas.objects.filter(user=nome_user)
   return render(request, 'view_user.html', data)

# Passa o dicionario CD para o View dos Abastecimentos (USER)
def view(request,pk):
    data = {}
    data['cd'] = Abastecimentos.objects.get(pk=pk)
    return render(request, 'view.html', data)

# Passa o dicionario BD para o View dos Abastecimentos (ADM)
def view_abastec(request):
    data = {}
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
     inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
     fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
     ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
     fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
     user = request.user.username
     data['bd'] = Abastecimentos.objects.filter(dia__range=[ini_date, fim_date])
    else:
     data['bd'] = Abastecimentos.objects.all()
    return render(request, 'view.html', data)

# Transmite o dicionario para a Tela de Recibos (ADM)
def view_cpadm(request):
    data = {}
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    filtro = request.GET.get('tipo_field')
    if start_date and end_date:
      inidt_date = datetime.strptime(start_date, '%Y-%m-%d')
      fimdt_date = datetime.strptime(end_date, '%Y-%m-%d')
      ini_date = datetime.strftime(inidt_date, '%d/%m/%Y')
      fim_date = datetime.strftime(fimdt_date, '%d/%m/%Y')
      data['db'] = RecibosPag.objects.filter(tipo=filtro, dia__range=[ini_date, fim_date])
    else:
      data['db'] = RecibosPag.objects.all()
    return render(request, 'recibosmoto.html', data)

# O Edit Permite o view e edição do form instanciado.
def edit(request, pk):
    data = {}
    data['db'] = Rotas.objects.get(pk=pk)
    data['bd'] = URotas.objects.all()
    data['modelos'] = Carros.objects.all()
    data['form'] = FormCliente(instance=data['db'])
    data['rotas'] = URotas.objects.all()
    return render(request, 'cadrota.html', data)

def edit_rcb(request, pk):
    data = {}
    data['rcb'] = 'rcb'
    data['db'] = RecibosPag.objects.get(pk=pk)
    data['form'] = FormRecibo(instance=data['db'])
    data['day'] = x.strftime('%d/%m/%Y')
    data['bd'] = User.objects.all()
    return render(request, 'cadrecibos.html', data)

def edit_abs(request, pk):
    data = {}
    data['db'] = Abastecimentos.objects.get(pk=pk)
    data['form'] = FormPedido(instance=data['db'])
    data['rota'] = URotas.objects.all()
    data['carros'] = Carros.objects.all()
    data['bd'] = User.objects.all()
    return render(request, 'cadabastecimentos.html', data)

def edit_urota(request, pk):
    data = {}
    data['editar'] = 'ed'
    data['db'] = URotas.objects.get(pk=pk)
    data['empresas'] = Empresa.objects.all()
    data['form'] = FormURotas(instance=data['db'])
    data['usuario'] = 'TEXTO'
    data['bd'] = User.objects.all()
    return render(request, 'cad_urotas.html', data)

def edit_empresa(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    data['form'] = FormEmpresa(instance=data['db'])
    return render(request, 'cad_empresa.html', data)

def edit_carro(request, pk):
    data = {}
    data['editar'] = 'ed'
    data['db'] = Carros.objects.get(id=pk)
    data['form'] = FormCarro(instance=data['db'])
    data['bd'] = User.objects.all()
    return render(request, 'cad_carro.html', data)

def edit_nf(request, pk):
   data = {}
   data['db'] = NotasRecebimento.objects.get(id=pk)
   data['bd'] = User.objects.all()
   data['form'] = FormNotas(instance=data['db'])
   return render(request, 'cad_nf.html', data)

def edit_perfil(request):
   data = {}
   data['db'] = Perfil.objects.get(user=request.user.id)
   data['form'] = FormPerfil(instance=data['db'])
   data['rota'] = URotas.objects.all()
   data['bd'] = User.objects.all()
   return render(request, 'cad_perfil.html', data)

def edit_perfil_moto(request):
   data = {}
   data['dbs'] = Perfil.objects.get(user=request.user.id)
   data['form'] = FormPerfil(instance=data['dbs'])
   data['rota'] = URotas.objects.all()
   data['bd'] = User.objects.all()
   return render(request, 'cad_perfil.html', data)

# O Update instancia o DATA e valida o FORM no DB
def update_abs(request, pk):
    data = {}
    data['db'] = Abastecimentos.objects.get(pk=pk)
    form = FormPedido(request.POST,request.FILES, instance=data['db'])
    if form.is_valid():
        form = form.save(commit=False)
        form.dia = request.POST.get('rday')
        form.carro = request.POST.get('rcarro')
        form.moto = request.POST.get('motofield')
        form.status = request.POST.get('rstatus')
        form.save()
        return redirect('abastecadm')
    
def update_nf(request, pk):
   data = {}
   data['db'] = NotasRecebimento.objects.get(id=pk)
   form = FormNotas(request.POST,request.FILES, instance=data['db'])
   if form.is_valid():
      form = form.save(commit=False)
      form.data = request.POST.get('rday')
      form.moto = request.POST.get('motocampo')
      form.save()
      return redirect('view_nf')

def update_empresa(request, pk):
   data = {}
   data['db'] = Empresa.objects.get(id=pk)
   form = FormEmpresa(request.POST, instance=data['db'])
   if form.is_valid():
      form = form.save(commit=False)
      form.save()
   return redirect('empresas')
    
def update_rcb(request, pk):
    data = {}
    data['db'] = RecibosPag.objects.get(pk=pk)
    form = FormRecibo(request.POST,request.FILES, instance=data['db']) 
    if form.is_valid():
        form = form.save(commit=False)
        form.moto = request.POST.get('motofield')
        form.dia = request.POST.get('rday')
        form.id_rota = request.POST.get('idrota')
        form.status = request.POST.get('stts')
        form.desc_pag = request.POST.get('rdesc')
        form.tipo = request.POST.get('rtipo')
        form.save()
        return redirect('recibospag')
    
def update_urota(request, pk):
   data = {}
   data['db'] = URotas.objects.get(id=pk)
   form = FormURotas(request.POST, instance=data['db'])
   if form.is_valid():
      form = form.save(commit=False)
      form.user = request.POST.get('motocampo')
      form.empresa = request.POST.get('transpcampo')
      form.save()
      return redirect('view_urotas')
   
def update_perfil(request, pk):
   data = {}
   data['db'] = Perfil.objects.get(id=pk)
   form = FormPerfil(request.POST,request.FILES, instance=data['db'])
   if form.is_valid():
      form = form.save(commit=False)
      form.user = request.POST.get('motocampo')
      form.save()
   return redirect('meu_perfil')

def update_perfil_moto(request, pk):
   data = {}
   data['db'] = Perfil.objects.get(id=pk)
   form = FormPerfil(request.POST,request.FILES, instance=data['db'])
   if form.is_valid():
      form = form.save(commit=False)
      form.user = request.user.id
      form.save()
   return redirect('meu_perfil')
   
def update_carro(request, pk):
   data = {}
   data['db'] = Carros.objects.get(id=pk)
   form = FormCarro(request.POST,request.FILES, instance=data['db'])
   if form.is_valid():
      form = form.save(commit=False)
      form.user = request.POST.get('motocampo')
      form.save()
      return redirect('view_urotas')

def update(request, pk):
    data = {}
    data['db'] = Rotas.objects.get(pk=pk)
    form = FormCliente(request.POST or None, instance=data['db'])   
    if form.is_valid():
        form = form.save(commit=False)
        form.dia = request.POST.get('uday')
        form.status = request.POST.get('rstatus')
    if 'nome_rota' and 'rcarro' in request.POST: 
        valor = request.POST.getlist('nome_rota')
        number = [float(sub.split('/')[0]) for sub in valor]
        valor_areceber = [float(sub.split('/')[3]) for sub in valor]
        lista = [str(sub.split('/')[1]) for sub in valor]
        carros = request.POST.getlist('rcarro')
        total = sum(number)
        form.vlr = total
        total_receber = sum(valor_areceber)
        form.receber_vlr = total_receber
        form.serv = ("," . join(lista))
        form.carro = ("," . join(carros))
        form.save()
        return redirect('rotadm')

def delete(request, pk):
    db = Rotas.objects.get(pk=pk)
    db.delete()
    return redirect('rotadm')

def deleteabastec(request, pk):
    bd = Abastecimentos.objects.get(pk=pk)
    bd.delete()
    return redirect('abastecadm')

def delrecibo(request, pk):
    bd = RecibosPag.objects.get(pk=pk)
    bd.delete()
    return redirect('recibospag')

def delete_user(request, pk):
   bd = User.objects.get(id=pk)
   bd.delete()
   return redirect('users')

def delete_urota(request, pk):
   bd = URotas.objects.get(id=pk)
   bd.delete()
   return redirect('view_urotas')

def delete_carro(request, pk):
   bd = Carros.objects.get(id=pk)
   bd.delete()
   return redirect('view_urotas')

def delete_nf(request, pk):
   bd = NotasRecebimento.objects.get(id=pk)
   bd.delete()
   return redirect('view_nf')

def delete_empresa(request, pk):
   bd = Empresa.objects.get(id=pk)
   bd.delete()
   return redirect('empresas')
