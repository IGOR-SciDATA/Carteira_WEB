from django.contrib import admin
from CarteiraApp.models import Vendas,Cliente,Loja,Produtos,Fornecedores,Promocoes

admin.site.site_header = 'Easy Control'
admin.site.site_title = 'Easy Control Controle Administrativo'
admin.site.index_title = "Seu sistema de dashboards completo!"

class VendasAdmin(admin.ModelAdmin):
    list_display = ('cod_vnd','data_vnd','cpf_cliente','cod_loja','cod_cliente','cod_pag','cod_promo','sku_prod','valor_total')
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cod_cliente','nome_cliente', 'data_nascimento','sexo_cliente','email_cliente','tel_cliente','cpf_cliente','profissao_cliente')

class LojaAdmin(admin.ModelAdmin):
    list_display = ('cod_loja','desc_loja','desc_uf','cidade','desc_bairro')

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome_prod','cod_prod', 'data_prod','cod_for','sku_prod')

class FornecedoresAdmin(admin.ModelAdmin):
    list_display = ('desc_for','cod_for','cnpj','uf','cidade')

class PromocoesAdmin(admin.ModelAdmin):
    list_display = ('cod_promo','nome_promo')

admin.site.register(Vendas, VendasAdmin)
admin.site.register(Promocoes, PromocoesAdmin)
admin.site.register(Fornecedores, FornecedoresAdmin)
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Loja, LojaAdmin)