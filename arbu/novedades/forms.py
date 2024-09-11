from django import forms
from empleados.models import EmpleadosModels

from .models import NovedadesModel

class NovedadesForm(forms.ModelForm):
    class Meta:
        model = NovedadesModel
        fields = [
            'iden',
            # 'nombres_empleado', 
            # 'apellidos_empleado', 
            'novedad_empleado', 
            'Fecha_inicio', 
            'Fecha_fin', 
            'soporte'
            
        ]
        widgets = {
            # 'nombres_empleado': forms.TextInput(attrs={'placeholder': 'Nombres del empleado'}),
            # 'apellidos_empleado': forms.TextInput(attrs={'placeholder': 'Apellidos del empleado'}),
            'novedad_empleado': forms.Select(),
            'Fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'soporte': forms.ClearableFileInput(),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['iden'].queryset = EmpleadosModels.objects.all()
            self.fields['iden'].label_from_instance = lambda obj: obj.identificacion
            self.fields['iden'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance