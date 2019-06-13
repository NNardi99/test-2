"""Importamos la clase HttpResponse"""
from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render

# """Definimos una función, cada función de vista toma al menos un parámetro request,
# el cuál es un objeto que contiene información sobre la vista que llama a la página actual,
# la cuál es una instancia de la clase Django.HttpRequest.
# En este ejemplo no hace nada el método request, no obstante siempre debe ser el primer parámetro de cualquier vista."""
# def hola(request):
#     return HttpResponse("Hola Mundo!")

# def fecha_actual(request):
#     ahora = datetime.datetime.now()
#     # html="<html><body><h1>Fecha:</h1><h3>%s<h/3></body></html>" % ahora
#     # t = get_template('fecha_actual.html')
#     # html = t.render({'fecha_actual': ahora})

#     return render(request, 'fecha_actual.html', {'fecha_actual': ahora})

# def horas_adelante(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
#     # html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset, dt.strftime("%H:%M:%S"))

#     return render(request, 'horas_adelante.html', {'horas_siguiente': dt, 'horas': offset})