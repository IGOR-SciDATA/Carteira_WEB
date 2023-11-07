from django.contrib import admin
from crudapp.models import URotas
from crudapp.models import Rotas,Perfil,Carros

admin.site.site_header = 'Spazio Transportes'
admin.site.site_title = 'Spazio Transportes'
admin.site.site_url = '/inicio/'
admin.site.index_title = "Seu sistema de gerenciamento completo!"

class RotasAdmin(admin.ModelAdmin):
    list_display = ('user', 'dia','carro','empresa','serv','status','vlr')
    
class URotasAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome','empresa','vlr')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome','cpf','rg')

class CarrosAdmin(admin.ModelAdmin):
    list_display = ('user','nome')

admin.site.register(URotas, URotasAdmin)
admin.site.register(Rotas, RotasAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Carros, CarrosAdmin)