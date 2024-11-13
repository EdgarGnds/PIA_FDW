from django.shortcuts import render, redirect
from .forms import EncuestaForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'ClashRoyale/index.html')

def cartas(request):
    return render(request, 'ClashRoyale/cartas.html')

def clanes(request):
    return render(request, 'ClashRoyale/clanes.html')

def esports(request):
    return render(request, 'ClashRoyale/esports.html')

def mazos(request):
    return render(request, 'ClashRoyale/mazos.html')

def encuesta_view(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            messages.success(request, 'Formulario enviado correctamente')  # Mensaje de éxito
            return redirect('inicio')  # Redirige a la página de inicio
        else:
            messages.error(request, 'Hubo un error con el formulario')  # Mensaje de error
    else:
        form = EncuestaForm()

    return render (request, 'ClashRoyale/esports.html', {'form': form})        
