from django.db import models


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.TextField()
    descripcion_larga = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    imagen_estatica = models.CharField(max_length=300, blank=True, help_text='Ruta relativa en static/img/, ej: img/dogo_post.jpg')
    imagen_extra = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    imagen_extra_estatica = models.CharField(max_length=300, blank=True)
    categoria = models.CharField(max_length=100)
    tags = models.CharField(max_length=300, blank=True)
    cliente = models.CharField(max_length=100, default='Dogo Armani')
    fecha = models.DateField()
    destacado = models.BooleanField(default=False)
    url_reel = models.URLField(blank=True, help_text='URL del Reel de Instagram (opcional)')
    orden = models.IntegerField(default=0)

    @staticmethod
    def _resolve_static(path):
        """Busca el archivo con .jpg, .jpeg o .png, devuelve la URL estatica."""
        import os
        from django.conf import settings
        from django.templatetags.static import static

        for staticdir in settings.STATICFILES_DIRS:
            full = os.path.join(str(staticdir), path)
            if os.path.isfile(full):
                return static(path)
        # Probar extensiones alternativas
        base, ext = os.path.splitext(path)
        alternativas = ['.jpg', '.jpeg', '.png', '.mp4', '.webm']
        for alt_ext in alternativas:
            if alt_ext != ext:
                alt_path = base + alt_ext
                for staticdir in settings.STATICFILES_DIRS:
                    full = os.path.join(str(staticdir), alt_path)
                    if os.path.isfile(full):
                        return static(alt_path)
        return static(path)

    def get_imagen_url(self):
        if self.imagen:
            return self.imagen.url
        if self.imagen_estatica:
            return self._resolve_static(self.imagen_estatica)
        return ''

    def get_imagen_extra_url(self):
        if self.imagen_extra:
            return self.imagen_extra.url
        if self.imagen_extra_estatica:
            return self._resolve_static(self.imagen_extra_estatica)
        return ''

    class Meta:
        ordering = ['orden', '-fecha']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.titulo


class Servicio(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    icono = models.CharField(max_length=10)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.titulo


class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['categoria', 'orden']
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    empresa = models.CharField(max_length=100, blank=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'

    def __str__(self):
        return f"{self.nombre} — {self.fecha:%d/%m/%Y}"
