from django.db import models

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
