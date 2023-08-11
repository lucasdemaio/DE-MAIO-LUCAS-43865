from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'aplicacion/base.html')


def autos(request):
    ctx = {"autos": Auto.objects.all()}
    return render(request, 'aplicacion/autos.html', ctx)

def motos(request):
    ctx = {"motos": Moto.objects.all()}
    return render(request, 'aplicacion/motos.html', ctx)

@login_required
def empleados(request):
    ctx = {"empleados": Empleado.objects.all()}
    return render(request, 'aplicacion/empleados.html', ctx)

@login_required
def clientes(request):
    ctx = {"clientes": Cliente.objects.all()}
    return render(request, 'aplicacion/clientes.html', ctx)

@login_required
def autosForm(request):
    if request.method == "POST":
        miForm = AutoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            auto = Auto(marca=informacion['marca'], modelo=informacion['modelo'], anio=informacion['anio'], kilometraje=informacion['kilometraje'])
            auto.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = AutoForm()      
    
    return render(request, "aplicacion/autosForm.html", {"form":miForm})

@login_required
def motosForm(request):
    if request.method == "POST":
        miForm = MotoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            moto = Moto(marca=informacion['marca'], modelo=informacion['modelo'], anio=informacion['anio'], kilometraje=informacion['kilometraje'])
            moto.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = MotoForm()      
    
    return render(request, "aplicacion/motosForm.html", {"form":miForm})

@login_required
def empleadosForm(request):
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            empleado = Empleado(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])
            empleado.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = EmpleadoForm()      
    
    return render(request, "aplicacion/empleadosForm.html", {"form":miForm})

@login_required
def clientesForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])
            cliente.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = ClienteForm()      
    
    return render(request, "aplicacion/clientesForm.html", {"form":miForm})


def buscarAuto(request):
    return render(request, "aplicacion/buscarAuto.html")

def buscarAuto2(request):
    if request.GET['marca']:
        marca = request.GET['marca']
        autos = Auto.objects.filter(marca__icontains=marca)
        return render(request, 
                      "aplicacion/resultadoBuscarAuto.html",
                      {"marca": marca, "autos":autos})
    
def buscarMoto(request):
    return render(request, "aplicacion/buscarMoto.html")

def buscarMoto2(request):
    if request.GET['marca']:
        marca = request.GET['marca']
        motos = Moto.objects.filter(marca__icontains=marca)
        return render(request, 
                      "aplicacion/resultadoBuscarMoto.html",
                      {"marca": marca, "motos":motos})
    
@login_required
def updateAuto(request, id_auto):
    auto = Auto.objects.get(id=id_auto)
    if request.method == "POST":
        miForm = AutoForm(request.POST)
        if miForm.is_valid():
            auto.marca = miForm.cleaned_data.get('marca')
            auto.modelo = miForm.cleaned_data.get('modelo')
            auto.anio = miForm.cleaned_data.get('anio')
            auto.kilometraje = miForm.cleaned_data.get('kilometraje')
            auto.save()
            return redirect(reverse_lazy('autos'))   
    else:
        miForm = AutoForm(initial={'marca':auto.marca, 
                                       'modelo':auto.modelo, 
                                       'anio':auto.anio, 
                                       'kilometraje':auto.kilometraje})         
    return render(request, "aplicacion/autosForm.html", {'form': miForm})

@login_required
def createAuto(request):    
    if request.method == "POST":
        miForm = AutoForm(request.POST)
        if miForm.is_valid():
            a_marca = miForm.cleaned_data.get('marca')
            a_modelo = miForm.cleaned_data.get('modelo')
            a_anio = miForm.cleaned_data.get('anio')
            a_kilometraje = miForm.cleaned_data.get('kilometraje')
            auto = Auto(marca=a_marca, 
                             modelo=a_modelo,
                             anio=a_anio,
                             kilometraje=a_kilometraje,
                             )
            auto.save()
            return redirect(reverse_lazy('autos'))
    else:
        miForm = AutoForm()

    return render(request, "aplicacion/autosForm.html", {"form":miForm})

@login_required
def updateMoto(request, id_moto):
    moto = Moto.objects.get(id=id_moto)
    if request.method == "POST":
        miForm = MotoForm(request.POST)
        if miForm.is_valid():
            moto.marca = miForm.cleaned_data.get('marca')
            moto.modelo = miForm.cleaned_data.get('modelo')
            moto.anio = miForm.cleaned_data.get('anio')
            moto.kilometraje = miForm.cleaned_data.get('kilometraje')
            moto.save()
            return redirect(reverse_lazy('motos'))   
    else:
        miForm = MotoForm(initial={'marca':moto.marca, 
                                       'modelo':moto.modelo, 
                                       'anio':moto.anio, 
                                       'kilometraje':moto.kilometraje})         
    return render(request, "aplicacion/motosForm.html", {'form': miForm})

@login_required
def createMoto(request):    
    if request.method == "POST":
        miForm = MotoForm(request.POST)
        if miForm.is_valid():
            m_marca = miForm.cleaned_data.get('marca')
            m_modelo = miForm.cleaned_data.get('modelo')
            m_anio = miForm.cleaned_data.get('anio')
            m_kilometraje = miForm.cleaned_data.get('kilometraje')
            moto = Moto(marca=m_marca, 
                             modelo=m_modelo,
                             anio=m_anio,
                             kilometraje=m_kilometraje,
                             )
            moto.save()
            return redirect(reverse_lazy('motos'))
    else:
        miForm = MotoForm()

    return render(request, "aplicacion/motosForm.html", {"form":miForm})

@login_required
def updateEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            empleado.nombre = miForm.cleaned_data.get('nombre')
            empleado.apellido = miForm.cleaned_data.get('apellido')
            empleado.email = miForm.cleaned_data.get('email')
            empleado.telefono = miForm.cleaned_data.get('telefono')
            empleado.save()
            return redirect(reverse_lazy('empleados'))   
    else:
        miForm = EmpleadoForm(initial={'nombre':empleado.nombre, 
                                       'apellido':empleado.apellido, 
                                       'email':empleado.email, 
                                       'telefono':empleado.telefono})         
    return render(request, "aplicacion/empleadosForm.html", {'form': miForm})

@login_required
def createEmpleado(request):    

    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            e_nombre = miForm.cleaned_data.get('nombre')
            e_apellido = miForm.cleaned_data.get('apellido')
            e_email = miForm.cleaned_data.get('email')
            e_telefono = miForm.cleaned_data.get('telefono')
            empleado = Empleado(nombre=e_nombre, 
                             apellido=e_apellido,
                             email=e_email,
                             telefono=e_telefono,
                             )
            empleado.save()
            return redirect(reverse_lazy('empleados'))
    else:
        miForm = EmpleadoForm()

    return render(request, "aplicacion/empleadosForm.html", {"form":miForm})

@login_required
def updateCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get('nombre')
            cliente.apellido = miForm.cleaned_data.get('apellido')
            cliente.email = miForm.cleaned_data.get('email')
            cliente.telefono = miForm.cleaned_data.get('telefono')
            cliente.save()
            return redirect(reverse_lazy('clientes'))   
    else:
        miForm = ClienteForm(initial={'nombre':cliente.nombre, 
                                       'apellido':cliente.apellido, 
                                       'email':cliente.email, 
                                       'telefono':cliente.telefono})         
    return render(request, "aplicacion/clientesForm.html", {'form': miForm})

@login_required
def deleteCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))

@login_required
def createCliente(request):    

    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            c_nombre = miForm.cleaned_data.get('nombre')
            c_apellido = miForm.cleaned_data.get('apellido')
            c_email = miForm.cleaned_data.get('email')
            c_telefono = miForm.cleaned_data.get('telefono')
            cliente = Cliente(nombre=c_nombre, 
                             apellido=c_apellido,
                             email=c_email,
                             telefono=c_telefono,
                             )
            cliente.save()
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clientesForm.html", {"form":miForm})

class AutoDetalle(LoginRequiredMixin, DetailView):
    model = Auto
    template_name = "aplicacion/autos_detail.html"

class MotoDetalle(LoginRequiredMixin, DetailView):
    model = Moto
    template_name = "aplicacion/motos_detail.html"

class EmpleadoDetalle(LoginRequiredMixin, DetailView):
    model = Empleado
    template_name = "aplicacion/empleados_detail.html"

class ClienteDetalle(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = "aplicacion/clientes_detail.html"

class AutoDelete(LoginRequiredMixin,DeleteView):
    model = Auto
    success_url = reverse_lazy('autos')

class MotoDelete(LoginRequiredMixin,DeleteView):
    model = Moto
    success_url = reverse_lazy('motos')

class ClienteDelete(LoginRequiredMixin,DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')

class EmpleadoDelete(LoginRequiredMixin,DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})

@login_required
def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm()

    return render(request, "aplicacion/registro.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
          
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})

def aboutme(request):
    return render(request, 'aplicacion/aboutme.html')