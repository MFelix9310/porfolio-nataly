from django.contrib import admin
from django.utils.html import format_html
from .models import Proyecto, Servicio, Habilidad, MensajeContacto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'preview_imagen', 'categoria', 'cliente', 'fecha', 'destacado', 'orden']
    list_filter = ['categoria', 'cliente', 'destacado']
    list_editable = ['orden', 'destacado']
    search_fields = ['titulo', 'descripcion']
    prepopulated_fields = {'slug': ('titulo',)}

    def preview_imagen(self, obj):
        url = obj.get_imagen_url()
        if url:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;" />', url)
        return '—'
    preview_imagen.short_description = 'Imagen'


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['icono', 'titulo', 'orden']
    list_editable = ['orden']


@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'orden']
    list_filter = ['categoria']
    list_editable = ['orden']


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'empresa', 'fecha', 'leido']
    list_filter = ['leido', 'fecha']
    search_fields = ['nombre', 'email', 'mensaje']
    list_editable = ['leido']
    readonly_fields = ['nombre', 'email', 'empresa', 'mensaje', 'fecha']
    actions = ['marcar_leido', 'marcar_no_leido']

    def marcar_leido(self, request, queryset):
        queryset.update(leido=True)
    marcar_leido.short_description = 'Marcar como leído'

    def marcar_no_leido(self, request, queryset):
        queryset.update(leido=False)
    marcar_no_leido.short_description = 'Marcar como no leído'

    def has_add_permission(self, request):
        return False
