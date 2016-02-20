from django.shortcuts import render
from .models import Prova
from .models import RespostaTest
from .models import Gymcana
# Create your views here.

def proves_gymcana(request,pk):
    
    proves = Prova.objects.filter(numgym=pk)
    gymcana = Gymcana.objects.get(pk=pk)
    return render(request, 'app/proves_gymcana.html', {'proves': proves, 'gymcana': gymcana})
def detalls_prova(request, idprova, pk):
    prova = Prova.objects.get(pk = idprova)
    respostes = RespostaTest.objects.filter(idpregunta = idprova)
    gymcana = Gymcana.objects.get(pk=pk)
    return render(request, 'app/detalls_prova.html', {'prova': prova, 'gymcana': gymcana, 'respostes': respostes})
