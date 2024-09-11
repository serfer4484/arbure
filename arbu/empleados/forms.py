from django import forms
from .models import EmpleadosModels,RolModel

# class EmpleadosForm(forms.Form):
#     nombres_empleado=forms.CharField(
#         max_length=200,
#         label="Nombres"
#         )
#     apellidos_empleado=forms.CharField(
#         max_length=200,
#         label="Apellidos"
#         )
#     identificacion=forms.IntegerField(
#         min_value=1000000000,
#         max_value=9999999999,
#         label="Número de Identificación"
#     )
#     sexo_empleado = forms.ChoiceField(
#         choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')],
#         label="Sexo"
#     )   
#     telefono_empleado = forms.CharField(
#         max_length=10,
#         label="Teléfono"
#     )
#     direccion_empleado=forms.CharField(
#         max_length=50,
#         label="Dirección"
#     )
#     email_empleado = forms.EmailField(
#         label="Correo Electrónico",           # Etiqueta que se mostrará en el formulario.
#         max_length=254,                       # Longitud máxima permitida para el campo.
#         required=True,                        # Indica si el campo es obligatorio. Por defecto, es True.
#         widget=forms.EmailInput(attrs={       # Personalización del widget HTML.
#             'placeholder': 'correo@ejemplo.com',  # Texto de sugerencia dentro del campo.
#             'class': 'form-control'                # Clase CSS para el estilo.
#         }),
#         error_messages={                      # Mensajes de error personalizados.
#             'required': 'Este campo es obligatorio.',
#             'invalid': 'Por favor, introduce una dirección de correo válida.'
#         },
#         help_text="Introduce una dirección de correo electrónico válida."
    
#     )
#     cargo_empleado = forms.CharField(
#         max_length=200,
#         label="Cargo"
#     )
#     ROLES_CHOICES = [(rol.id, rol.roles) for rol in RolModel.objects.all()]

#     rol_empleado = forms.ChoiceField(
#         choices=ROLES_CHOICES,
#         label="Rol del Empleado",
#         required=True
#     )
#     salario_empleado = forms.DecimalField(
#         max_digits=10,
#         decimal_places=2, 
#         initial=0.00,
#     ) 
#     contacto_emergencia=forms.CharField(
#         max_length=200,
#         label="Contacto de emergencias"
#     )
#     tel_emergencia=forms.CharField(
#         max_length=10,
#         label="Teléfono de Emergencias"
#           )
#     foto_empleado = forms.ImageField(
#         label='Foto del Empleado',
#         required=False
#         )
#     def save(self, commit=True):
#         # Obtiene el rol seleccionado
#         rol_id = self.cleaned_data.get('rol_empleado')
#         try:
#             rol_instance = RolModel.objects.get(id=rol_id)
#         except RolModel.DoesNotExist:
#             rol_instance = None

#         # Crea una instancia del modelo de empleado
#         empleado_instance = EmpleadosModels(
#             nombres_empleado=self.cleaned_data['nombres_empleado'],
#             apellidos_empleado=self.cleaned_data['apellidos_empleado'],
#             identificacion=self.cleaned_data['identificacion'],
#             sexo_empleado=self.cleaned_data['sexo_empleado'],
#             telefono_empleado=self.cleaned_data['telefono_empleado'],
#             direccion_empleado=self.cleaned_data['direccion_empleado'],
#             email_empleado=self.cleaned_data['email_empleado'],
#             cargo_empleado=self.cleaned_data['cargo_empleado'],
#             rol_empleado=rol_instance,  # Asocia el rol al empleado
#             salario_empleado=self.cleaned_data['salario_empleado'],
#             contacto_emergencia=self.cleaned_data['contacto_emergencia'],
#             tel_emergencia=self.cleaned_data['tel_emergencia'],
#             foto_empleado=self.cleaned_data['foto_empleado']
#         )
        
#         if commit:
#             empleado_instance.save()

#         return empleado_instance
    
# from django import forms
# from .models import EmpleadosModels, RolModel

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = EmpleadosModels
        fields = ['nombres_empleado', 'apellidos_empleado', 'identificacion', 'sexo_empleado', 
                  'telefono_empleado', 'direccion_empleado', 'email_empleado', 'cargo_empleado', 
                  'rol_empleado', 'salario_empleado', 'contacto_emergencia', 'tel_emergencia', 
                  'foto_empleado']

    def __init__(self, *args, **kwargs):
        super(EmpleadosForm, self).__init__(*args, **kwargs)
        # Personalizar el queryset del campo 'rol_empleado'
        self.fields['rol_empleado'].queryset = RolModel.objects.all()

    def save(self, commit=True):
        empleado_instance = super().save(commit=False)
        if commit:
            empleado_instance.save()
        return empleado_instance

