from django.contrib import admin
from .models import Page

#configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)

#configuración del panel
title = "Proyecto con Django"
subtitle = "Panel de Gestión"

admin.site.site_header = title #Título
admin.site.site_title = title #Subtitulo
admin.site.index_title = subtitle #Título en la página

