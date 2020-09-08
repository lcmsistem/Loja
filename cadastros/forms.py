from django.forms import ModelForm, TextInput, Textarea, Form
from django import forms
from .models import Fornecedor, Centro, Grupo, Contas, Lancamento
from django.contrib.admin.widgets import AdminDateWidget

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = [ 'codf',
                   'nome',
                   'cnpj',
                   'ende',
                   'bairro',
                   'cidade',
                   'estado',
                   'ddd',                   
                   'fone',
                   'cep',
                   'email',
                   'centro',
                   'cadastro'
                   ]
 
        labels = {'codf' : 'Código',
                  'nome' : 'Nome:',
                  'cnpj' : 'C.N.P.J.:',
                  'ende' : 'Endereço:',
                  'bairro' : 'Bairro',
                  'cidade' : 'Cidade:',
                  'estado' : 'Estado:',
                  'fone' : 'Telefone:',
                  'cep' : 'CEP:',
                  'ddd' : 'DDD:' ,
                  'centro' : 'Centro de Custo',
                  'cadastro' : 'Data do Cadastro'
        }   

        widgets = {
            'codf': Textarea(attrs={'cols': 10, 'rows': 1}),
            'nome': Textarea(attrs={'cols': 80, 'rows': 1}),
            'cnpj': Textarea(attrs={'cols': 14, 'rows': 1}),
            'ende': Textarea(attrs={'cols': 100, 'rows': 1}),
            'bairro': Textarea(attrs={'cols': 30, 'rows': 1}),
            'cidade': Textarea(attrs={'cols': 100, 'rows': 1}),
            'fone': Textarea(attrs={'cols': 12, 'rows': 1}),
            'cep': Textarea(attrs={'cols': 8, 'rows': 1}),
            'ddd': Textarea(attrs={'cols': 2, 'rows': 1}),
            'cadastro': AdminDateWidget()
         }

class CentroForm(ModelForm):
    class Meta:
        model = Centro
        fields = ['centro', 'nome','despesa','empresa','nivel2','perfil']

        widgets = {
            'centro': Textarea(attrs={'cols': 7, 'rows': 1}),
            'nome': Textarea(attrs={'cols': 50, 'rows': 1}),
            'despesa': Textarea(attrs={'cols': 1, 'rows': 1}),
            'empresa': Textarea(attrs={'cols': 1, 'rows': 1}),
            'nivel2': Textarea(attrs={'cols': 3, 'rows': 1}),
            'perfil': Textarea(attrs={'cols': 1, 'rows': 1}),
         }


class Formulario(forms.Form):
    centro = forms.CharField(label='Centro de Custo',required=False)
    nome = forms.CharField(label='Descrição',required=False)
    despesa = forms.CharField(label='Despesa',required=False)
    empresa = forms.CharField(label='Empresa:     1-Atelier        2-Guanabara        3-Nova Campinas ', required=False)
    nivel2 = forms.CharField(required=False, label='Nível 2')
    perfil = forms.CharField(required=False, label='Perfil  -    D-DESPESA       R-RECEITA')

    def save(self, commit=True):
        if commit:
            self.save()
        return ''   

class FormGrupo(ModelForm):
    class Meta:
        model = Grupo
        fields = ['grupo','nome']

        labels = {'grupo' : 'Código do Grupo',
                  'nome'  : 'Descrição do Grupo'}

        widgets = {'codf': Textarea(attrs={'cols': 2, 'rows': 1}),
                   'nome': Textarea(attrs={'cols': 80, 'rows': 1})
        }

class FormEdita(forms.Form):
    grupo = forms.CharField(label='Código do Grupo',required=False)
    nome = forms.CharField(label='Descrição',required=False)

    def save(self, commit=True):
        if commit:
            self.save()
        return ''

class FormContas(ModelForm):
    class Meta:
        model = Contas
        fields = ['conta','banco','agencia','obs1', 'obs2', 'saldoinicial','saldofinal', 'limite', 'tipo' ]
        labels = {
            'conta' : 'Número da Conta',
            'banco' : 'Nº Banco',
            'agencia' : 'Agência',
            'obs1' : 'Titular da Conta',
            'obs2' : 'Informações adicionais',
            'saldoinicial' : 'Saldo Inicial',
            'saldoatual' : 'Saldo Atual',
            'limite' : 'Limite',
            'tipo' : 'Tipo: 1-Corrente   2-Investimentos   3-Outras '
        }

class FormLancamento(ModelForm):
    class Meta:
        model = Lancamento
        fields = ['conta','dia','historico','documento','valor']
        labels = {'conta': 'Conta nº',
                  'dia': 'Data',
                  'historico':' Histórico',
                  'documento': 'Documento',
                  'valor': 'Valor - R$'
        }
        widgets = { 'dia': AdminDateWidget() }
