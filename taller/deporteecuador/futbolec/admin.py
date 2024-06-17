from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Equipo, Jugador, Campeonato, CampeonatoEquipos
from import_export import resources 

# Recursos para import_export (opcional si decides usarlo)
class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo

class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador

class CampeonatoResource(resources.ModelResource):
    class Meta:
        model = Campeonato

class CampeonatoEquiposResource(resources.ModelResource):
    class Meta:
        model = CampeonatoEquipos

# Clases de administración
class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Si decides utilizar import_export, descomenta la línea resource_class
    # resource_class = EquipoResource
    list_display = ('nombre', 'siglas', 'username')
    search_fields = ('nombre', 'siglas', 'username')

class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Si decides utilizar import_export, descomenta la línea resource_class
    # resource_class = JugadorResource
    list_display = ('nombre', 'posicion', 'numero_camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'posicion', 'equipo__nombre')

class CampeonatoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Si decides utilizar import_export, descomenta la línea resource_class
    # resource_class = CampeonatoResource
    list_display = ('nombre_campeonato', 'nombre_auspiciante')
    search_fields = ('nombre_campeonato', 'nombre_auspiciante')

class CampeonatoEquiposAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Si decides utilizar import_export, descomenta la línea resource_class
    # resource_class = CampeonatoEquiposResource
    list_display = ('anyo', 'equipo', 'campeonato')
    search_fields = ('anyo', 'equipo__nombre', 'campeonato__nombre_campeonato')

# Registro de modelos
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
