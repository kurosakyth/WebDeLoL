from django.db import models

# Create your models here.
#captura la estructura la tabla libros en este caso

class Fondo(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to = 'images/', verbose_name='Imagen',null = True)
    titulo = models.CharField(max_length=100, verbose_name='Título', null = True)

