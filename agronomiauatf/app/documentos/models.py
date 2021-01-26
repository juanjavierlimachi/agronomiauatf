from django.db import models
from django.contrib.auth.forms import User
from datetime import date
# Create your models here.
class Categoria(models.Model):
    """Model definition for Categoria  ."""
    Nombre_categoria = models.CharField('Categoria', max_length=100,unique=True)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Categoria   ."""

        verbose_name = 'Categoria  '
        verbose_name_plural = 'Categorias'

    '''def get_absolute_url(self):
        return ('tutorial_view_sample', [self.id]) '''
    
    def __str__(self):
        """Unicode representation of Categoria ."""
        return self.Nombre_categoria
    
class Documento(models.Model):
    """Model definition for Documento."""
    Titulo = models.CharField('Titulo', max_length=150)
    Categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    #Descripcion = models.TextField(max_length=200, blank=True, null=True)
    Archivo = models.FileField('Archivo', upload_to='archivos', max_length=100, help_text="Adjunte el archivo a guardar")
    Usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    Privado = models.BooleanField('Privado',help_text="El documento es oculto para los usuarios ", default = False)
    
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    
    Descargas = models.IntegerField(default = 0)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Documento."""
        ordering = ('-id',)
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        """Unicode representation of Documento."""
        return self.Titulo

class Comentar(models.Model):
    """Model definition for Comentar."""
    Descripcion = models.TextField(max_length=200,help_text="Describa de que trata el documento")
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_mod = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default = True)
    Usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete = models.CASCADE)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Comentar."""

        verbose_name = 'Comentar'
        verbose_name_plural = 'Comentars'

    def __str__(self):
        """Unicode representation of Comentar."""
        return self.Descripcion

class Compartir(models.Model):
    """Model definition for Compartir."""
    Asunto = models.CharField('Asunto', max_length=150)
    Descripcion = models.TextField(max_length=200,help_text="Describa de que trata el documento")
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_mod = models.DateTimeField(auto_now=True)
    Correo_origen = models.EmailField('Origen', max_length=200)
    Correo_Destino = models.EmailField('Ingrese el correo', max_length=200)
    estado = models.BooleanField(default = True)
    Usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete = models.CASCADE)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Compartir."""

        verbose_name = 'Compartir'
        verbose_name_plural = 'Compartirs'

    def __str__(self):
        """Unicode representation of Compartir."""
        return self.Asunto
