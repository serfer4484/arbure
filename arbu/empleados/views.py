from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView

from .forms import EmpleadosForm
from .models import EmpleadosModels

class EmpleadosFormView(generic.FormView):
    template_name = "empleados/empleados.html"
    form_class =EmpleadosForm
    success_url = reverse_lazy("empleados")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
            
            print(form.errors)  
            return super().form_invalid(form)

class EmpleadosListView(generic.ListView):
    model=EmpleadosModels
    template_name = "empleados/lista_empleados.html"
    context_object_name="lista_empleados"

class EmpleadosUpdateView(UpdateView):
    model = EmpleadosModels
    form_class = EmpleadosForm
    template_name = 'empleados/editar_empleado.html'
    success_url = reverse_lazy('empleados')

class EmpleadosDeleteView(DeleteView):
    model = EmpleadosModels
    template_name = 'empleados/eliminar_empleado.html'  # Esta plantilla puede no ser necesaria si usas confirmación con JavaScript
    success_url = reverse_lazy('lista_empleados')  # Redirigir después de eliminar

    # Si no deseas utilizar una plantilla para confirmación, puedes sobrescribir el método delete:
    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()
    #     return redirect(self.success_url)