from django.contrib import admin
from .models import DetalleVenta, Venta

from ventas.forms import MyForm, VentasForm

from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import inch, cm
from reportlab.platypus import Table, TableStyle
import time

# Register your models here.

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 10
    max_num = 10
    form = MyForm
    
    # The inlines can't be changed or deleted
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        js = (
            # '//unpkg.com/axios/dist/axios.min.js', # axios
            'js/loadSelect.js',       # project static folder
        )

class VentaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Fecha de Venta', {'fields': ['fecha']}),
        ('Vendedor', {'fields': ['vendedor']}),
        ('Cliente', {'fields': ['cliente']}),
        # ('Estado', {'fields': ['estado']}),
    ]

    inlines = [
        DetalleVentaInline,
    ]

    form = VentasForm
    
    def export_sells_as_pdf(self, request, queryset):

        file_name = "sell_entries{0}.pdf".format(time.strftime("%d-%m-%Y-%H-%M-%S"))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)

        data = [['codigo', 'vendedor', 'cliente', 'fecha']]
        for d in queryset.all():
            item = [d.codigo, d.vendedor, d.cliente, d.fecha]
            data.append(item)

        doc = SimpleDocTemplate(response, pagesize=(21*inch, 29*inch))
        elements = []

        sell_data = Table(data)
        sell_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                        ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
                                        ("FONTSIZE",  (0, 0), (-1, -1), 13)]))
        elements.append(sell_data)
        doc.build(elements)

        return response
    export_sells_as_pdf.short_description = "Exportar Ventas como PDF"

    list_display = ('codigo', 'vendedor', 'cliente', 'fecha')
    search_fields = ('vendedor_id__first_name', 'vendedor_id__last_name', 'cliente_id__razon')
    list_filter = ('vendedor', 'cliente', 'fecha')
    actions = [export_sells_as_pdf, ]
    ordering = ('codigo',)
    change_list_template = 'admin/change_list_graph_sell.html'


admin.site.register(Venta, VentaAdmin)