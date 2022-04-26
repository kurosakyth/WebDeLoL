from django.db import models

# Create your models here.
#captura la estructura la tabla libros en este caso

class Fondo(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to = 'images/', verbose_name='Imagen',null = True)
    titulo = models.CharField(max_length=100, verbose_name='Título', null = True)

    def __str__(self):
        fila = "Título: " + self.titulo
        return fila
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()