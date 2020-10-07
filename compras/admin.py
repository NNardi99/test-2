from django.contrib import admin
from .models import DetalleCompra, Compra

from compras.forms import MyForm, ComprasForm

from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import inch, cm
from reportlab.platypus import Table, TableStyle
import time

# Register your models here.

class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 10
    max_num = 10
    form = MyForm
    
    # The inlines can't be changed or deleted
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class CompraAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Fecha de Compra', {'fields': ['fecha']}),
        ('Comprador', {'fields': ['comprador']}),
        ('Proveedor', {'fields': ['proveedor']}),
        # ('Estado', {'fields': ['estado']}),
    ]

    inlines = [
        DetalleCompraInline,
    ]

    form = ComprasForm

    def export_buys_as_pdf(self, request, queryset):

        file_name = "buy_entries{0}.pdf".format(time.strftime("%d-%m-%Y-%H-%M-%S"))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)

        data = [['codigo', 'comprador', 'proveedor', 'fecha']]
        for d in queryset.all():
            item = [d.codigo, d.comprador, d.proveedor, d.fecha]
            data.append(item)

        doc = SimpleDocTemplate(response, pagesize=(21*inch, 29*inch))
        elements = []

        buy_data = Table(data)
        buy_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                        ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
                                        ("FONTSIZE",  (0, 0), (-1, -1), 13)]))
        elements.append(buy_data)
        doc.build(elements)

        return response
    export_buys_as_pdf.short_description = "Exportar Compras como PDF"

    list_display = ('codigo', 'comprador', 'proveedor', 'fecha')
    search_fields = ('comprador_id__first_name', 'comprador_id__last_name', 'proveedor_id__razon')
    list_filter = ('comprador', 'proveedor', 'fecha')
    actions = [export_buys_as_pdf, ]
    ordering = ('codigo',)
    change_list_template = 'admin/change_list_graph_buy.html'

admin.site.register(Compra, CompraAdmin)