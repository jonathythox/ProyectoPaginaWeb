from django.shortcuts import render
from .models import Marca, Telefono, TelefonoInstance

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_telefonos=Telefono.objects.all().count()
    num_instances=TelefonoInstance.objects.all().count()
    # TELEFONOS disponibles (status = 'd')
    num_instances_available=TelefonoInstance.objects.filter(status__exact='d').count()
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_telefonos':num_telefonos,'num_instances':num_instances,'num_instances_available':num_instances_available},
    )
