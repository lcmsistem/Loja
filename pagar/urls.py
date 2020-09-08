from django.urls import path
from .views import pagar, alterar_pagar, filtra_pagar, excluir_pagar, lancar_pagar, incluir_pagar
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('filtra_pagar', filtra_pagar, name='url_filtrapagar'),
    path('pagar/', pagar, name='url_pagar'),
    path('alterar_pagar/<int:pk>', alterar_pagar, name='url_altpagar'),
    path('excluir_pagar/<int:pk>', excluir_pagar, name='url_excpagar'),
    path('lancar_pagar/<int:pk>', lancar_pagar, name='url_lctpagar'),
    path('incluir_pagar/', incluir_pagar, name='url_incpagar'),
    ]