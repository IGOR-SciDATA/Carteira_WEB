from django.forms import ModelForm
from django import forms
import crudapp.models as Models

class FormCliente(ModelForm):
    class Meta:
        model = Models.Rotas
        fields = []

class FormPedido(ModelForm):
   class Meta:
        model = Models.Abastecimentos
        fields = ['km','img','vlr']

class FormRecibo(ModelForm):
    class Meta:
        model = Models.RecibosPag
        fields = ['rcb']

class FormCarro(ModelForm):
    class Meta:
        model = Models.Carros
        fields = ['nome','photo']

class FormURotas(ModelForm):
    class Meta:
        model = Models.URotas
        fields = ['nome','vlr','receber_vlr']

class FormPerfil(ModelForm):
    class Meta:
        model = Models.Perfil
        fields = ['nome','cpf','rg','end','foto','foto_selfie','cnh']

class FormEmpresa(ModelForm):
    class Meta:
        model = Models.Empresa
        fields = ['nome','endereco']

class FormNotas(ModelForm):
    class Meta:
        model = Models.NotasRecebimento
        fields = ['pdf']