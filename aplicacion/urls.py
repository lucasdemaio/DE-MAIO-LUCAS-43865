from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),
    path('autos', autos, name="autos"),
    path('motos', motos, name="motos"),
    path('empleados', empleados, name="empleados"),
    path('clientes', clientes, name="clientes"),

    path('autos_form', autosForm, name="autos_form"),
    path('motos_form', motosForm, name="motos_form"),
    path('empleados_form', empleadosForm, name="empleados_form"),
    path('clientes_form', clientesForm, name="clientes_form"),

    path('buscar_autos', buscarAuto, name="buscar_autos"),
    path('buscarAuto2', buscarAuto2, name="buscarAuto2"),

    path('buscar_motos', buscarMoto, name="buscar_motos"),
    path('buscarMoto2', buscarMoto2, name="buscarMoto2"),

    path('update_auto/<id_auto>/', updateAuto, name="update_auto"),
    path('create_auto', createAuto, name="create_auto"),
    

    path('update_moto/<id_moto>/', updateMoto, name="update_moto"),
    path('create_moto', createMoto, name="create_moto"),

    path('update_empleado/<id_empleado>/', updateEmpleado, name="update_empleado"),
    path('create_empleado', createEmpleado, name="create_empleado"),

    path('update_cliente/<id_cliente>/', updateCliente, name="update_cliente"),
    path('create_cliente', createCliente, name="create_cliente"),

    path('detail_auto/<int:pk>/', AutoDetalle.as_view(), name="detail_auto"),
    path('detail_moto/<int:pk>/', MotoDetalle.as_view(), name="detail_moto"),
    path('detail_empleado/<int:pk>/', EmpleadoDetalle.as_view(), name="detail_empleado"),
    path('detail_cliente/<int:pk>/', ClienteDetalle.as_view(), name="detail_cliente"),

    path('delete_auto/<int:pk>/', AutoDelete.as_view(), name="delete_auto"),
    path('delete_moto/<int:pk>/', MotoDelete.as_view(), name="delete_moto"),
    path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente"),
    path('delete_empleado/<int:pk>/', EmpleadoDelete.as_view(), name="delete_empleado"),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', register, name="register"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),

    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('aboutme/', aboutme, name="aboutme"),
    

]