from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Creación de la vista para registrar usuarios
class SignUpView(CreateView):
    # Formulario personalizado para pedir usuario, correo y contraseña
    form_class = CustomUserCreationForm
    # Plantilla HTML que renderizará el formulario de registro
    template_name = 'registration/signup.html'
    # Redireccionar a la vista de login una vez completado el registro
    success_url = reverse_lazy('login')
