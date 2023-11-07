"""
URL configuration for crudweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings 
from django.urls import path, include
from crudapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('', include('pwa.urls')),
    path('cad_users/', views.cad_users, name='cad_users'),
    path('login/', views.painel, name='painel'),
    path('logar/', views.logar, name='logar'),
    path('store/', views.store, name='store'),
    path('logout/', views.logouts, name='logouts'),
    path('rotas/', views.home, name='home'),
    path('rotasadm/', views.rotadm, name='rotadm'),
    path('abastecimentosadm/', views.abastecadm, name='abastecadm'),
    path('recibos/', views.recibospag, name='recibospag'),
    path('inicio/', views.inicio, name='inicio'),
    path('cad_rota/', views.cad_rota, name='cad_rota'),
    path('criar_perfil/', views.cad_perfil, name='cad_perfil'),
    path('create_perfil/', views.create_perfil, name='create_perfil'),
    path('cad_recibos/', views.cad_recibo, name='cad_recibo'),
    path('cad_nf/', views.cad_nf, name='cad_nf'),
    path('cad_nfadm/', views.cad_nfadm, name='cad_nfadm'),
    path('create_nf/', views.create_nf, name='create_nf'),
    path('create_nfadm/', views.create_nfadm, name='create_nfadm'),
    path('create/', views.create, name='create'),
    path('create_r/', views.create_r, name='create_r'),
    path('create_rcb/', views.create_rcb, name='create_rcb'),
    path('create_rw/', views.create_rw, name='create_rw'),
    path('create_carro/', views.create_carro, name='create_car'),
    path('abastecimentos/view/<int:pk>/', views.view, name='view'),
    path('abastecimentos/', views.abastec, name='abastec' ),
    path('abastecimentosadm/view/<int:pk>/', views.view, name='view'),
    path('recibos/view/<int:pk>/', views.viewrec, name='viewrec'),
    path('viewuser/<str:nome_user>/', views.viewmoto, name="viewmoto"),
    path('view_urotas', views.view_urotas, name='view_urotas'),
    path('view_nf', views.view_nf, name='view_nf'),
    path('edituser/', views.edit_user, name='edituser'),
    path('editurota/<int:pk>/', views.edit_urota, name='edit_urota'),
    path('editempresa/<int:pk>/', views.edit_empresa, name='edit_empresa'),
    path('edit_perfil/', views.edit_perfil, name='edit_user'),
    path('edit_perfil_moto/', views.edit_perfil_moto, name='edit_perfil_moto'),
    path('editnf/<int:pk>/', views.edit_nf, name='edit_nf'),
    path('editcarro/<int:pk>/', views.edit_carro, name='edit_carro'),
    path('addcarro/<int:pk>/', views.cad_carro, name='cadcarro'),
    path('addcarro/', views.add_carro, name='add_carro'),
    path('add_carro/', views.create_add_carro, name='create_add_carro'),
    path('editmoto/<int:pk>/', views.edit_moto, name='edit_moto'),
    path('abastecimentosadm/', views.abastecadm, name='abastecadm' ),
    path('notasabastecimento/', views.view_abastec, name='view_abastec'),
    path('comprovantes/', views.view_cp, name='view_cp'),
    path('comprovantesadm/', views.view_cpadm, name='view_cpadm'),
    path('addempresa/', views.add_empresa, name='add_empresa'),
    path('create_empresa/', views.create_empresa, name='create_empresa'),
    path('cad_abastecimento/', views.cad_abastecimento, name='cad_abastecimento'),
    path('payoil/', views.pay_oil, name='pay_oil'),
    path('payrota/', views.pay_rota, name='pay_rota'),
    path('receiverota/', views.receive_rota, name='receive_rota'),
    path('addrota/<int:pk>/', views.cad_urotas, name='cad_urotas'),
    path('addrota/', views.add_urotas, name='add_urota'),
    path('add_rota/', views.create_add_rota, name='create_add_rota'),
    path('users/', views.users, name='users'),
    path('empresas/', views.empresas, name='empresas'),
    path('perfil/', views.meu_perfil, name='meu_perfil'),
    path('perfil/<int:pk>/', views.view_motorista, name='view_motorista'),
    path('create_p/', views.create_p, name='create_p'),
    path('create_urota/', views.create_urotas, name='creat_urout'),
    path('update/<int:pk>/', views.update, name='update'),
    path('updaterota/', views.update_all, name='update_all'),
    path('updateuser/', views.update_moto, name='update_moto'),
    path('updatenf/<int:pk>/', views.update_nf, name='update_nf'),
    path('update_perfil/<int:pk>/', views.update_perfil, name='update_perfil'),
    path('update_perfil_moto/<int:pk>/', views.update_perfil_moto, name='update_perfil_moto'),
    path('update_urota/<int:pk>/', views.update_urota, name='update_urota'),
    path('update_empresa/<int:pk>/', views.update_empresa, name='update_empresa'),
    path('update_carro/<int:pk>/', views.update_carro, name='update_carro'),
    path('deleteuser/<int:pk>/', views.delete_user, name='delete_user'),
    path('deleteurota/<int:pk>/', views.delete_urota, name='delete_urota'),
    path('deletecarro/<int:pk>/', views.delete_carro, name='delete_carro'),
    path('deleteempresa/<int:pk>/', views.delete_empresa, name='delete_empresa'),
    path('deletenf/<int:pk>/', views.delete_nf, name='delete_nf'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('recibos/edit/<int:pk>/', views.edit, name='edit'),
    path('updatercb/<int:pk>/', views.edit_rcb, name='edit_rcb'),
    path('save/<int:pk>/', views.update_rcb, name='update_rcb'),
    path('updateabs/<int:pk>/', views.edit_abs, name='edit_abs'),
    path('saveabs/<int:pk>/', views.update_abs, name='update_abs'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('deleteabastec/<int:pk>/', views.deleteabastec),
    path('deleterecibo/<int:pk>/', views.delrecibo),
]

if settings.DEBUG:
    urlpatterns += static (
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT)
