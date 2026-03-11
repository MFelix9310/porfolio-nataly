from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db import models
from .models import Proyecto, Servicio, Habilidad
from .forms import ContactoForm


def home(request):
    proyectos = Proyecto.objects.all()
    servicios = Servicio.objects.all()
    habilidades = Habilidad.objects.all()
    form = ContactoForm()

    habilidades_por_categoria = {}
    for h in habilidades:
        habilidades_por_categoria.setdefault(h.categoria, []).append(h)

    # Reels: proyectos con categoria 'Reel' o que tengan url_reel o sean video
    reels = proyectos.filter(
        models.Q(categoria='Reel') | models.Q(url_reel__gt='')
    ).distinct()

    # Excluir reels del portfolio principal
    proyectos_portfolio = proyectos.exclude(categoria='Reel')

    return render(request, 'core/home.html', {
        'proyectos': proyectos_portfolio,
        'servicios': servicios,
        'habilidades_por_categoria': habilidades_por_categoria,
        'form': form,
        'reels': reels,
    })


def proyecto_detalle(request, slug):
    proyecto = get_object_or_404(Proyecto, slug=slug)
    return render(request, 'core/proyecto_detalle.html', {
        'proyecto': proyecto,
    })


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'ok': True, 'mensaje': '¡Gracias! Te respondo en menos de 24 horas.'})
            return render(request, 'core/home.html', {
                'form': ContactoForm(),
                'mensaje_exito': '¡Gracias! Te respondo en menos de 24 horas.',
                'proyectos': Proyecto.objects.all(),
                'servicios': Servicio.objects.all(),
                'habilidades_por_categoria': {},
            })
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'ok': False, 'errores': form.errors}, status=400)
    return JsonResponse({'ok': False}, status=405)
