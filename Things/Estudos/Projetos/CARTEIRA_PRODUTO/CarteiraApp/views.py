from django.shortcuts import render
from CarteiraApp.models import Cliente

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def clientes_dash(request):
    return render(request,'dashboard_cliente.html')