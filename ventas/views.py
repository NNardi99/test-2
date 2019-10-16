from django.shortcuts import render
from django.views.generic import TemplateView
from ventas.models import DetalleVenta
from django.db.models import Sum
# Create your views here.
class Get5Products(TemplateView):
    template_name = "grafica_5_ventas.html"

    def get_context_data(self,**kwargs):
        context = super(Get5Products,self).get_context_data(**kwargs)  
        context['top_five']=DetalleVenta.objects.values('producto', 'producto__nombre').annotate(sum_prod=Sum('cantidad')).order_by('sum_prod')[:5]
        return context