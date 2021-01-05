from django.utils.timezone import now
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    position = models.CharField(max_length=200, verbose_name="Cargo", null=True, blank=True)
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Enlace", null=True, blank=True)
    start_date = models.DateField(verbose_name="Fecha de Inicio", default=now, null=True, blank=True)
    end_date = models.DateField(verbose_name="Fecha de Finalizacion", default=now, null=True, blank=True)
    owned_project = models.BooleanField(default=False)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["order", "created"]

    def __str__(self):
        return self.title