import datetime
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView,ListView
from django.shortcuts import get_object_or_404

from empleados.models import EmpleadosModels
from .forms import TurnosForms
from .models import TurnosModel

class TurnosViews(FormView):
    form_class = TurnosForms
    template_name = 'turnos/turnos.html'
    # success_url = reverse_lazy('turnos')
    success_url = reverse_lazy('lista_turnos_semana')


    def form_valid(self, form):
    
        form.save()
        return super().form_valid(form)
    

class TurnosSemanaView(TemplateView):
    template_name = 'turnos/lista_turnos_semana.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener el empleado seleccionado por cédula
        empleado_id = self.request.GET.get('empleado_id')
        if empleado_id:
            empleado = get_object_or_404(EmpleadosModels, id=empleado_id)
            turnos = TurnosModel.objects.filter(identifi=empleado)
        else:
            turnos = TurnosModel.objects.all()

        # Pasar los turnos directamente al contexto
        context['turnos'] = turnos
        context['empleado_id'] = empleado_id  
        context['empleados'] = EmpleadosModels.objects.all()  
        return context
