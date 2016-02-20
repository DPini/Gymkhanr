from django.shortcuts import render
from .models import Prova
from .models import Gymcana
# Create your views here.

def proves_gymcana(request,pk):

    proves = Prova.objects.filter(numgym=pk)
    gymcana = Gymcana.objects.get(pk=pk)
    return render(request, 'app/proves_gymcana.html', {'proves': proves, 'gymcana': gymcana})
def detalls_prova(request, idprova, pk):
    prova = Prova.objects.get(pk = idprova)
    gymcana = Gymcana.objects.get(pk=pk)
    return render(request, 'app/detalls_prova.html', {'prova': prova, 'gymcana': gymcana})

from .forms import ProvaCodiForm

def realitza_prova_codi(request):
    if request.method == 'POST':
        form = ProvaCodiForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("http://google.com")
        else
            form = ProvaCodiForm();
        return render(request,'app/realitza_prova_codi.html', {'form': form})
