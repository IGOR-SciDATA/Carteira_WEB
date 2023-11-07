from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class URotas(models.Model):
    user = models.CharField(max_length=60, blank=True)
    nome = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60, blank=True)
    vlr = models.FloatField(max_length=6)
    receber_vlr = models.FloatField(max_length=6, default=None)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Perfil(models.Model):
    user = models.CharField(max_length=60, null=True)
    nome = models.CharField(max_length=60, null=True)
    cpf = models.CharField(max_length=14, null=True)
    rg = models.CharField(max_length=12, null=True)
    end = models.CharField(max_length=60, null=True)
    foto = models.ImageField('foto',upload_to='docs', null=True)
    foto_selfie = models.ImageField('selfie',upload_to='self', null=True)
    cnh = models.FileField('cnhs', upload_to='cnhs', null=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfil'

class Rotas(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default='a')
    dia = models.CharField(max_length=10)
    carro = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60, blank=True)
    serv = models.CharField(max_length=60)
    status = models.CharField(max_length=60, blank=True)
    receber_vlr = models.FloatField(max_length=6, default=None)
    vlr = models.FloatField(max_length=6)
 
    class Meta:
        verbose_name = 'Rotas Diaria'
        verbose_name_plural = 'Rotas Diarias'

class Carros(models.Model):
    user = models.CharField(max_length=60, blank=True)
    nome = models.CharField(max_length=60)
    photo = models.ImageField('photo',upload_to='carros', null=True)

    class Meta:
        verbose_name = 'Modelos Cadastrados'
        verbose_name_plural = 'Modelos Cadastrados'

class RecibosPag(models.Model):
    moto = models.CharField(max_length=60, blank=True)
    dia = models.CharField(max_length=60)
    desc_pag = models.CharField(max_length=60, blank=True)
    status = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    rcb = models.ImageField('rcb',upload_to='recibos')

class Abastecimentos(models.Model):
    moto = models.CharField(max_length=60, blank=True)
    dia = models.CharField(max_length=10)
    carro = models.CharField(max_length=60)
    vlr = models.FloatField(max_length=4, null=True)
    status = models.CharField(max_length=60, null=True)
    km = models.ImageField('km', upload_to='km')
    img = models.ImageField('bomba', upload_to='bomba')

class Empresa(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=60)

class NotasRecebimento(models.Model):
    moto = models.CharField(max_length=60)
    data = models.CharField(max_length=10)
    pdf = models.FileField('notas', upload_to='notas')