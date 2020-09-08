from django.forms import ModelForm, TextInput, Textarea, Form
from django import forms
from cadastros.models import Fornecedor, Centro, Pagar
from django.contrib.admin.widgets import AdminDateWidget

class PagarForm(ModelForm):

    class Meta:
        model = Pagar
        fields = '__all__'
        labels = {'pagnume' : 'Número', 'pagnota' : 'Número da Nota Fiscal',
                  'pagcodf': 'Fornecedor/Credor', 'pagcent' : 'Centro de Custo',
                  'pagduli': 'Duplicata nº', 'pagobs' : 'Observação',
                  'pagbanc': 'Banco', 'pagvalor' : 'Valor',
                  'pagcheq': 'Nº do Cheque', 'pagvalp' : 'Valor Pago',
                  'pagcont': 'Contato', 'pagdesc' : 'Valor do Desconto',
                  'pagconta': 'Conta Bancária', 'pagtaxa' : 'Taxa de Desconto',
                  'pagsitu': 'Situação - L-lançada', 'pagabat' : 'Abatimento',
                  'pagcomo': 'Forma de Pagamento', 'paglimi' : 'Data limite do desconto',
                  'pagvenc': 'Vencimento', 'pagpaga':'Data de Pagamento',
                  'pagdata': 'Data de Emissão'}

        widgets = {'pagdata': AdminDateWidget(),
                   'pagvenc': AdminDateWidget(),
                   'pagpaga': AdminDateWidget(),
                   'paglimi': AdminDateWidget()}

