from django.shortcuts import render
from .models import Prova,ProvaCodi,ProvaTest
from .models import RespostaTest
from .models import Gymcana
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def proves_gymcana(request,pk):

    proves = Prova.objects.filter(numgym=pk)
    gymcana = Gymcana.objects.get(pk=pk)
    return render(request, 'app/proves_gymcana.html', {'proves': proves, 'gymcana': gymcana})
def detalls_prova(request, idprova, pk):
    prova = Prova.objects.get(pk = idprova)
    gymcana = Gymcana.objects.get(pk=pk)
    if prova.tipo == 2:
        prova = ProvaTest.objects.get(pk = idprova)
        respostes = RespostaTest.objects.filter(idpregunta = idprova)
        #return render(request, 'app/detalls_prova.html', {'prova': prova, 'gymcana': gymcana, 'respostes': respostes})
        from .forms import ProvaTestForm
        if request.method == 'POST':
            form = ProvaTestForm(request.POST,idprova=idprova)
            if form.is_valid():
                resposta = form.cleaned_data['resposta']
                if resposta.id == prova.respostacorrecta:
                    prova.superada = 1
                    prova.save()
                from django.http import HttpResponseRedirect
                return HttpResponseRedirect(".")
        else:
            form = ProvaTestForm(idprova=idprova);
            return render(request,'app/detalls_prova.html', {'form': form, 'prova': prova, 'gymcana': gymcana})
    if prova.tipo == 1:
        prova = ProvaCodi.objects.get(pk = idprova)
        from .forms import ProvaCodiForm
        if request.method == 'POST':
            form = ProvaCodiForm(request.POST)
            if form.is_valid():
                codi = form.cleaned_data['CodiIntr']
                if codi == prova.codi :
                    prova.superada = 1
                    prova.save()
                from django.http import HttpResponseRedirect
                return HttpResponseRedirect(".")
        else:
            form = ProvaCodiForm();
            return render(request,'app/detalls_prova.html', {'form': form, 'prova': prova, 'gymcana': gymcana})


"""
def realitza_prova_codi(request):
    if request.method == 'POST':
        form = ProvaCodiForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("http://google.com")
        else
            form = ProvaCodiForm();
        return render(request,'app/realitza_prova_codi.html', {'form': form})
"""
