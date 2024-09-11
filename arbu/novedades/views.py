from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from .forms import NovedadesForm
from .models import NovedadesModel

class NovedadesFormViews(generic.FormView):
    form_class = NovedadesForm
    template_name = 'novedades/novedades.html'
    context_object_name = 'novedades'
    success_url = reverse_lazy('novedades')  # Reemplaza 'success_url' con tu URL de éxito

    def form_valid(self, form):
        
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        
        print(form.errors)  
        return super().form_invalid(form)
    
class NovedadesListView(ListView):
    model = NovedadesModel
    template_name = 'novedades/lista_novedades.html'
    context_object_name = 'novedades'


