# Create your models here.
from django.db import models

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    sexo_cliente = models.CharField(max_length=2)
    email_cliente = models.CharField(max_length=60)
    tel_cliente = models.IntegerField(max_length=13)
    cpf_cliente = models.IntegerField(max_length=11)
    profissao_cliente = models.CharField(max_length=60)
    
class Produtos(models.Model):
    data_prod = models.DateField()
    cod_grupo = models.IntegerField(max_length=1)
    cod_dep = models.IntegerField(max_length=1)
    cod_for = models.IntegerField(max_length=1)
    cod_loja = models.IntegerField(max_length=1)
    desc_grupo = models.CharField(max_length=20)
    desc_dep = models.CharField(max_length=20)
    sku_prod = models.IntegerField(max_length=1)
    nome_prod = models.CharField(max_length=60)
    modelo_prod = models.CharField(max_length=60)
    cor_prod = models.CharField(max_length=60)
    tam_prod = models.CharField(max_length=3)
    est_prod = models.CharField(max_length=15)

class Loja(models.Model):
    cod_reg = models.IntegerField(max_length=1)
    cod_prod = models.CharField(max_length=2)
    desc_loja = models.CharField(max_length=60)
    desc_uf = models.CharField(max_length=60)
    desc_reg = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=60)

class Fornecedores(models.Model):
    cnpj = models.IntegerField(max_length=14)
    desc_for  = models.CharField(max_length=60)
    cod_produto = models.IntegerField(max_length=60)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)

class Vendas(models.Model):
    data_vnd = models.DateField()
    cpf_cliente = models.IntegerField(max_length=11)
    cod_loja = models.IntegerField(max_length=1)
    cod_cliente = models.IntegerField(max_length=1)
    cod_pag = models.IntegerField(max_length=1)
    cod_promo = models.IntegerField(max_length=1, blank=True)
    sku_prod = models.IntegerField(max_length=1)
    valor_total = models.FloatField(max_length=6)