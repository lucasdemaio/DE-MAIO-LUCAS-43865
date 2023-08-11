from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutoForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    anio = forms.IntegerField(label="Año", required=True)
    kilometraje = forms.IntegerField(label="Kilometraje", required=True)

class MotoForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    anio = forms.IntegerField(label="Año", required=True)
    kilometraje = forms.IntegerField(label="Kilometraje", required=True)

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        help_texts = { k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)  