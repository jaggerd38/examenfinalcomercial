from django.contrib import admin
from notas.models import Profesor, Materia, MateriaAdmin, Grado, GradoAdmin, Alumno, Pensum

admin.site.register(Profesor)
admin.site.register(Pensum)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.autodiscover()
