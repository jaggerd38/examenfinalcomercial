from django import forms

from .models import Grado, Materia

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('grado', 'seccion', 'descripcion', 'materias')

    def __init__ (self, *args, **kwargs):

        super(GradoForm, self).__init__(*args, **kwargs)

        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].queryset = Materia.objects.all()
        self.fields["materias"].help_text = "SELECCIONE LAS MATERIAS DEL GRADO"
