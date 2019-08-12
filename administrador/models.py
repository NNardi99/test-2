from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator
# Create your models here.

class QuerySetManager(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            obj.is_active = True
            obj.save()
        #super(ImageQuerySet, self).delete(*args, **kwargs)

class Provincia(models.Model):
    provincia = models.CharField(max_length=100)

    class Meta:
        ordering = ["provincia"]
    
    def __str__(self):
        return self.provincia

class Localidad(models.Model):
    localidad = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ["provincia"]
        verbose_name_plural = "Localidades"
        
    def __str__(self):
        return self.localidad

class CustomUser(AbstractUser):
    cuil = models.CharField(max_length=13, validators=[RegexValidator(r'^[0-9]{2}-[0-9]{8}-[0-9]$','El número ingresado es incorrecto','Número incorrecto')])
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$','El número ingresado es incorrecto','Número incorrecto')])
    domicilio = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, null = True, on_delete=models.PROTECT)
    localidad = ChainedForeignKey(
        Localidad,
        chained_field="provincia",
        chained_model_field="provincia",
        show_all=False,
        auto_choose=True,
        sort=True,
        null = True,
        on_delete=models.PROTECT
    )
    
    def get_short_name(self):
        return self.username

    def natural_key(self):
        return self.username
    
    # manager = QuerySetManager.as_manager()
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        # print (self.is_active)
        self.save()
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self):
        return '%s %s'% (self.first_name, self.last_name)

class Cliente(models.Model):
    razon = models.CharField(max_length=200)
    cuit = models.CharField(max_length=13, validators=[RegexValidator(r'^[0-9]{2}-[0-9]{8}-[0-9]$','El número ingresado es incorrecto','Número incorrecto')])
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$','El número ingresado es incorrecto','Número incorrecto')])
    email = models.EmailField(blank=True, verbose_name='e-mail')
    domicilio = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    localidad = ChainedForeignKey(
        Localidad,
        chained_field="provincia",
        chained_model_field="provincia",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.PROTECT
    )
    contacto = models.CharField(blank=True, max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.razon

class Proveedor(models.Model):
    razon = models.CharField(max_length=200)
    cuit = models.CharField(max_length=13, validators=[RegexValidator(r'^[0-9]{2}-[0-9]{8}-[0-9]$','El número ingresado es incorrecto','Número incorrecto')])
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$','El número ingresado es incorrecto','Número incorrecto')])
    email = models.EmailField(blank=True, verbose_name='e-mail')
    domicilio = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    localidad = ChainedForeignKey(
        Localidad,
        chained_field="provincia",
        chained_model_field="provincia",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.PROTECT
    )
    contacto = models.CharField(blank=True, max_length=100)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Proveedores"
        
    def __str__(self):
        return self.razon

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Categoría de Productos"
        verbose_name_plural = "Categorías de Productos"
    
    def __str__(self):
        return self.nombre

class Riesgo(models.Model):
    riesgo = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Tipo de Riesgo"
        verbose_name_plural = "Tipos de Riesgos"
    
    def __str__(self):
        return self.riesgo

class Marca(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre

STOCK_UNIT_CHOICES = [('1','unidades'), ('2','pares'), ('3','litros')]

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=1000, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name='categoría del producto')
    riesgo = models.ForeignKey(Riesgo, on_delete=models.PROTECT, verbose_name='tipo de riesgo')
    stockMin = models.PositiveIntegerField(verbose_name='stock mínimo', default=1, validators=[MinValueValidator(1)])
    stockMax = models.PositiveIntegerField(verbose_name='stock máximo', default=1, validators=[MinValueValidator(1)])
    stockAct = models.PositiveIntegerField(verbose_name='stock disponible', default=1, validators=[MinValueValidator(1)])
    unidad = models.CharField(max_length=100, choices=STOCK_UNIT_CHOICES)
    imagen = models.ImageField(upload_to='./static')

    def image_tag(self):
        return mark_safe('<div style="background-image: url(\'/%s\'); width: 50px; height: 50px; background-repeat: no-repeat; background-size: contain; background-position: center"></div>'% (self.imagen))
    image_tag.short_description = 'Imagen'

    def __str__(self):
        return self.nombre