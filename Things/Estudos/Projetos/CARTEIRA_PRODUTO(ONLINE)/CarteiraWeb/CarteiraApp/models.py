# Create your models here.
from django.db import models

class Cliente(models.Model):
    def __str__(self):
        return str(self.cod_cliente)
    
    cod_cliente = models.IntegerField(null=False, blank=False, default=0)
    nome_cliente = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    sexo_cliente = models.CharField(max_length=60)
    email_cliente = models.CharField(max_length=60)
    tel_cliente = models.CharField(null=False, blank=False,default='', max_length=60)
    cpf_cliente = models.CharField(null=False, blank=False,default='', max_length=60)
    profissao_cliente = models.CharField(max_length=60)

class Fornecedores(models.Model):
    def __str__(self):
        return str(self.cod_for)
    
    cod_for = models.IntegerField(null=False, blank=False, default=0)
    cnpj = models.CharField(max_length=60)
    desc_for  = models.CharField(max_length=60)
    uf = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)

class Produtos(models.Model):
    def __str__(self):
        return str(self.cod_prod)
    
    cod_prod = models.IntegerField(null=False, blank=False,default=0)
    data_prod = models.DateField()
    cod_for = models.ForeignKey(Fornecedores, related_name='codfor', on_delete=models.CASCADE)
    sku_prod = models.IntegerField(null=False, blank=False,default=0)
    nome_prod = models.CharField(max_length=60)
    modelo_prod = models.CharField(max_length=60)
    cor_prod = models.CharField(max_length=60)
    tam_prod = models.CharField(max_length=60)

class Loja(models.Model):
    def __str__(self):
        return str(self.cod_loja)
    
    cod_loja = models.IntegerField(null=False, blank=False,default=0)
    desc_loja = models.CharField(max_length=60)
    desc_bairro = models.CharField(max_length=60)
    desc_uf = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)

class Promocoes(models.Model):
    def __str__(self):
        return str(self.cod_promo)
    
    cod_promo = models.IntegerField(null=False, blank=False, default=0)
    nome_promo = models.CharField(max_length=60)

class Vendas(models.Model):
    def __str__(self):
        return str(self.cod_vnd)
    
    cod_vnd = models.IntegerField(null=False, blank=False,default=0)
    data_vnd = models.DateField()
    cpf_cliente = models.CharField(null=False, blank=False,default='', max_length=60)
    cod_loja = models.ForeignKey(Loja, related_name='codloja', on_delete=models.CASCADE)
    cod_cliente = models.ForeignKey(Cliente, related_name='codcliente', on_delete=models.CASCADE)
    cod_pag = models.IntegerField(null=False, blank=False,default=0)
    cod_promo = models.ForeignKey(Promocoes, related_name='codpromo', on_delete=models.CASCADE, null=True,blank=True)
    sku_prod = models.ForeignKey(Produtos, related_name='skuprod', on_delete=models.CASCADE)
    valor_total = models.FloatField(max_length=60)