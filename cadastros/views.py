from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fornecedor, Centro, Grupo, Contas, Lancamento
from .forms import FornecedorForm, CentroForm, Formulario, FormGrupo, FormContas, FormLancamento
from .cnpj import validar_cnpj, validar_cpf



# Create your views here.
@login_required(login_url='/home')
def menu_cadastro(request):
    return render(request, 'menu.html')

@login_required(login_url='/home')
def fornecedor(request):
    listafor = Fornecedor.objects.raw('SELECT CODF,NOME,CIDADE from fornecedor order by nome')
    return render(request, 'fornecedor.html', {'Fornecedor': listafor})    

@login_required(login_url='/home')
def teste(request):
    form = Formulario(request.POST or None)
    form.data.nome = 'teste'
    canc = request.POST.get('cancelar')
    erro = False
    if canc != 'cancelar':
        if form.is_valid():
            dados = form.data
            ct = Centro.objects.filter(centro=dados['centro'] )
            if ct:
                print('--> ' + str(ct))
                erro = True
                return render(request, 'teste.html', {'form': form, 'erro': erro})
            else:
                ceto = Centro(centro=dados['centro'],
                      nome=dados['nome'],
                      despesa=dados['despesa'],
                      empresa=dados['empresa'],
                      perfil=dados['perfil'],
                      nivel2=dados['nivel2']
                )
                ceto.save()
                return redirect('url_cadastrocus')
    else:
        if canc=='cancelar':
           print('cancelou')
           return redirect('url_cadastrocus')

    return render(request, 'teste.html', {'form': form})

@login_required(login_url='/home')
def submenu(request):
    form = Formulario(request.POST or None)
    if form.is_valid():
       f = request.POST.get('nome')
       print(f)
       #form.save()
       return redirect('menu')
    return render(request, 'submenu.html', {'form': form})

@login_required(login_url='/home')
def atualiza_fornecedor(request,pk):
    #data = {}
    fornecedor = Fornecedor.objects.get(pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    cancelar = request.POST.get('cancelar')
    if cancelar=='cancelar':
        return redirect('url_cadastrofor')
    if form.is_valid():
        form.save(commit=False)
        dados = form.data
        fcnpj = request.POST.get('cnpj')
        if validar_cnpj(fcnpj):
           if dados['codf']==pk:
              form.save()
              return redirect('url_cadastrofor')
           else:
              erro = True
              msg = 'Você não pode alterar o código do fornecedor'
              return render(request, 'telafor.html', {'form':form, 'erro':erro, 'mensagem':msg})
        else:
           erro = True
           msg = 'O cnpj está incorreto. Verifique'
           return render(request, 'telafor.html', {'form':form, 'erro':erro, 'mensagem':msg})
    return render(request, 'telafor.html', {'form':form})


@login_required(login_url='/home')
def inclui_fornecedor(request):
    valido=True
    ult = Fornecedor.objects.latest('pk').pk
    ultimo = int(ult)
    if ultimo > 1000:
        ultimo = ultimo + 1
    ultimo = '0'+str(ultimo)
    erro = False
    if request.method == 'POST':
        form = FornecedorForm(request.POST or None)
        dados = form.data
        if form.is_valid():
            if dados['codf']==ultimo:
               fcnpj = request.POST.get('cnpj')
               if validar_cnpj(fcnpj):
                  form.save()
                  return redirect('url_cadastrofor')
               else:
                  msg = 'O C.N.P.J. está incorreto. Verifique!'
                  erro = True
            else:
               msg = 'O Código deve ser ' + ultimo
               erro = True
        if erro:
           return render(request, 'telafor.html',{'form':form, 'ultimo':ultimo,  'erro':erro, 'mensagem':msg})
    else:
        form = FornecedorForm()

    return render(request, 'telafor.html',{'form':form, 'ultimo':ultimo, 'erro':erro})


@login_required(login_url='/home')
def consulta_fornecedor(request):
    lista = ''
    query = request.GET.get('busca')
    print(query)
    if query!='':
       lista = Fornecedor.objects.filter(nome__icontains=query)
       return render(request, 'consulta.html', {'lista':lista}) 
    else:
       listafor = Fornecedor.objects.raw('SELECT CODF,NOME,CIDADE from fornecedor order by nome')     
    return render(request, 'fornecedor.html', {'Fornecedor': listafor})   


@login_required(login_url='/home')
def custo(request):    
    lista = Centro.objects.all()
    retorno = request.GET.get('botao')
    if (retorno=='menu'):
        return redirect('url_teste')
    return render(request, 'custo.html', {'custo': lista})    


@login_required(login_url='/home')
def manut_custo(request, pk):
     #data = {}
    custo = Centro.objects.get(pk=pk)
    form = CentroForm(request.POST or None, instance=custo)
    cancelar = request.POST.get('cancelar')

    if cancelar=='cancelar':
        return redirect('menu')
    if form.is_valid():
        form.save()
        return redirect('url_cadastrocus')
    #data['form'] = form     
    return render(request, 'manut_custo.html', {'form':form})   

def vsql(request):
    sql = Fornecedor.objects.raw('SELECT CODF,NOME,CNPJ from fornecedor order by nome')
    return render(request, 'sql.html', {'vsql': sql})    

def mostra_imagem(request):
    return render(request, 'imagem.html') 


@login_required(login_url='/home')
def mostra_centro(request):
    sql = Centro.objects.all()
    print(sql)
    return render(request, 'centro.html', {'centro': sql})


@login_required(login_url='/home')
def exclui_centro(request, pk):
    centro = get_object_or_404(Centro, pk=pk)
    c = request.POST.get('cancelar')
    if c=='cancelar':
       return redirect('url_cadastrocus')

    if request.method == 'POST':
        centro.delete()
        return redirect('url_cadastrocus')

    return render(request,'exclui_centro.html', {'centro': centro})


@login_required(login_url='/home')
def exclui_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    c = request.POST.get('cancelar')
    if c=='cancelar':
       return redirect('url_cadastrofor')

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('url_cadastrofor')

    return render(request,'exclui_fornecedor.html', {'fornecedor': fornecedor})


@login_required(login_url='/home')
def grupo(request):
    listagru = Grupo.objects.raw('SELECT GRUPO,NOME from GRUPO order by GRUPO')
    retorno = request.GET.get('botao')
    if (retorno=='menu'):
        return redirect('url_incgrupo')
    return render(request, 'grupo.html', {'grupo': listagru})


@login_required(login_url='/home')
def inc_grupo(request):
    form = FormGrupo(request.POST or None)
    canc = request.POST.get('cancelar')
    erro = False
    if canc != 'cancelar':
        if form.is_valid():
            dados = form.data
            ct = Grupo.objects.filter(grupo=dados['grupo'] )
            if ct:
                print('--> ' + str(ct))
                erro = True
                return render(request, 'menu.html', {'form': form, 'erro': erro})
            else:
                ceto = Grupo(grupo=dados['grupo'],
                      nome=dados['nome'],
                )
                ceto.save()
                return redirect('url_grupo')
    else:
        if canc=='cancelar':
           print('cancelou')
           return redirect('url_grupo')

    return render(request, 'inc_grupo.html', {'form': form})


def exclui_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    c = request.POST.get('cancelar')
    if c=='cancelar':
       return redirect('url_grupo')

    if request.method == 'POST':
        grupo.delete()
        return redirect('url_grupo')

    return render(request,'exclui_grupo.html', {'grupo': grupo})

@login_required(login_url='/home')
def altera_grupo(request, pk):
     #data = {}
    grupo = Grupo.objects.get(pk=pk)
    #form = FormGrupo(request.POST or None)
    form = FormGrupo(request.POST or None, instance=grupo)
    cancelar = request.POST.get('cancelar')

    if cancelar=='cancelar':
        return redirect('url_grupo')
    if form.is_valid():
        form.save()
        return redirect('url_grupo')
    #data['form'] = form
    return render(request, 'altera_grupo.html', {'form':form})


@login_required(login_url='/home')
def contas(request):
   contas = Contas.objects.all()
   return render(request, 'contas.html', {'contas':contas})

@login_required(login_url='/home')
def altera_conta(request, pk):
    conta = Contas.objects.get(pk=pk)
    form = FormContas(request.POST or None, instance=conta)
    if form.is_valid():
        form.save()
        return redirect('url_conta')
    return render(request, 'altera_conta.html', {'form':form})

@login_required(login_url='/home')
def incluir_conta(request):
    form = FormContas(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_conta')
    return render(request, 'inc_conta.html', {'form': form})

@login_required(login_url='/home')
def lancamentos(request, cta):
    lanca = Lancamento.objects.raw('SELECT LANCAMENTO,CONTA,DIA,HISTORICO,DOCUMENTO,VALOR FROM LANCAMENTO WHERE CONTA=%s ORDER BY CONTA,DIA',[cta])
    return render(request, 'lancamentos.html', {'lanca':lanca})
