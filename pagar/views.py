from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cadastros.models import Intervalo, Pagar, Fornecedor, Centro, Grupo, Lancamento
from .forms import *
from datetime import date, datetime, timedelta
from django.db import connection, transaction


# Create your views here.

@login_required(login_url='/home')
def filtra_pagar(request):
    inicio =  date.today()-timedelta(days=5)
    fim =  date.today()+timedelta(days=10)
    return render(request, 'filtrapagar.html', {'inicio':inicio, 'fim':fim})

def grava_pagperiodo(usuario,comeco,final):
    usu = str(usuario)
    nome = Intervalo.objects.filter(user=usu)
    for k in nome:
        n = k.id
    if nome:
       crsor = connection.cursor()
       crsor.execute('UPDATE intervalo SET pagini=%s, pagfim=%s WHERE id=%s',[comeco, final, n])
       connection.commit()
    else:
        itv = Intervalo(
              user=str(usuario),
              pagini=comeco,
              pagfim=final,
              lctini=comeco,
              lctfim=final
              )
        itv.save()

@login_required(login_url='/home')
def pagar(request):
    inicio = request.GET.get('inicio')  # date.today()-timedelta(days=10)
    fim = request.GET.get('fim')  # date.today()+timedelta(days=30)
    retorno = request.GET.get('botao')
    if (retorno=='novo'):
        return redirect('url_incpagar')

    if not inicio:
        usu = str(request.user)
        nome = Intervalo.objects.filter(user=usu)
        for k in nome:
            inicio = k.pagini
            fim = k.pagfim
    else:
        grava_pagperiodo(request.user, inicio, fim)
    contas = Pagar.objects.raw('SELECT * FROM PAGAR WHERE PAGVENC>=%s AND PAGVENC<=%s ORDER BY PAGVENC',[inicio,fim])
    return render(request, 'pagar.html', {'contas':contas})

@login_required(login_url='/home')
def alterar_pagar(request,pk):
    conta = Pagar.objects.get(pk=pk)
    form = PagarForm(request.POST or None, instance=conta)
    cancelar = request.POST.get('cancelar')
    erro=False
    msg=''
    if cancelar=='cancelar':
        return redirect('url_pagar')
    if form.is_valid():
        form.save()
        return redirect('url_pagar')
    else:
        erro = True
        msg = 'O cnpj está incorreto. Verifique'

    return render(request, 'alterar_pagar.html', {'form':form, 'erro':erro,'mensagem':msg})


@login_required(login_url='/home')
def excluir_pagar(request, pk):
    conta = get_object_or_404(Pagar, pk=pk)
    c = request.POST.get('cancelar')
    if c == 'cancelar':
        return redirect('url_pagar')
    if request.method == 'POST':
       conta.delete()
       return redirect('url_pagar')

    return render(request, 'exclui_pagar.html', {'conta': conta})


@login_required(login_url='/home')
def lancar_pagar(request, pk):
    cta = Pagar.objects.get(pk=pk)
    cc = connection.cursor()
    cc.execute('select p.pagcodf,p.pagcent,p.pagconta,f.nome from pagar p, fornecedor f where p.pagnume=%s and p.pagcodf=f.codf',[pk])
    for k in cc:
        vcentro = (k[1])
        vcodf = (k[0])
        vconta = (k[2])
        vhisto = (k[3])
    c = request.POST.get('cancelar')
    if c == 'cancelar':
        return redirect('url_pagar')
    if request.method == 'POST':        # ATUALIZA SITUACAO DA CONTA
        vhisto = vcodf + '-' + vhisto[0:23]
        crsor = connection.cursor()
        crsor.execute('UPDATE PAGAR SET pagsitu=%s WHERE pagnume=%s', ['L', pk])
        connection.commit()

        # ATUALIZA LANÇAMENTOS E SALDO DA CONTA
        crsor.execute('INSERT INTO LANCAMENTO (dia,valor,centrocusto,documento,historico,caiu, conta) VALUES (%s,%s,%s,%s,%s,%s,%s)', [cta.pagpaga,(-1)*cta.pagvalor,vcentro,cta.pagnota,vhisto,'S',vconta])
        connection.commit()
        return redirect('url_pagar')

    return render(request, 'lancar.html', {'conta': cta})

@login_required(login_url='/home')
def incluir_pagar(request):
    form = PagarForm(request.POST or None)
    c = request.POST.get('cancelar')
    if c == 'cancelar':
        return redirect('url_pagar')
    if form.is_valid():
       form.save()
       print('salvou')
       return redirect('url_pagar')
    return render(request, 'inc_pagar.html', {'form':form})