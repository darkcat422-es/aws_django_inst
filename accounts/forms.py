from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'autofocus': True})
    )

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            # Autenticar buscando al usuario mediante su email
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Por favor, introduzca un correo electrónico y una contraseña correctos."
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data