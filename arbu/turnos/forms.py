from django import forms
from .models import TurnosModel
from empleados.models import EmpleadosModels

class TurnosForms(forms.ModelForm):
    class Meta:
        model = TurnosModel
        fields = ['identifi', 'Fecha_inicio', 'Fecha_fin', 'hora_inicio', 'hora_fin']
        widgets = {
            'Fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio':forms.TimeInput(attrs={'type':'time'}),
            'hora_fin':forms.TimeInput(attrs={'type':'time'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['identifi'].queryset = EmpleadosModels.objects.all()
        self.fields['identifi'].label_from_instance = lambda obj: obj.identificacion
        self.fields['identifi'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
