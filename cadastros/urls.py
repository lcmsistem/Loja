from django.urls import path
from .views import *
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('menu/', menu_cadastro, name='menu'),
    path('fornecedor/', fornecedor, name='url_cadastrofor'),
    path('custo/', custo, name='url_cadastrocus'),
    path('newfor/', inclui_fornecedor, name='url_newfor'),
    path('update/<str:pk>', atualiza_fornecedor , name='url_updatefor'),
    path('consulta/', consulta_fornecedor, name='url_consultafor'),
    path('manut_custo/<str:pk>', manut_custo, name='url_man_custo'),
    path('sql/', vsql, name='url_sql'),
    path('centro/', mostra_centro, name='url_centro'),
    path('imagem/', mostra_imagem, name='url_imagem'), 
    path('teste/', teste, name='url_teste'),
    path('sub/', submenu, name='url_submenu'),
    path('exclui_centro/<str:pk>', exclui_centro, name='url_excluicentro'),
    path('exclui_fornecedor/<str:pk>', exclui_fornecedor, name='url_excfor'),
    path('grupo/', grupo, name='url_grupo'),
    path('inc_grupo/', inc_grupo, name='url_incgrupo'),
    path('exc_grupo/<str:pk>', exclui_grupo, name='url_excgrupo'),
    path('alt_grupo/<str:pk>', altera_grupo, name='url_altgrupo'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('contas/', contas, name='url_conta'),
    path('alt_conta/<str:pk>', altera_conta, name='url_altconta'),
    path('inc_conta//', incluir_conta, name='url_incconta'),
    path('lancamentos/<str:cta>', lancamentos, name='url_lancamento'),
]

