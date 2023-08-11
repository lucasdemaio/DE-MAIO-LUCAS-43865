# Proyecto Final

Autor: Lucas De Maio
Nombre: Proyecto Final

Objetivo del TP:
Crear una aplicación con Django (estilo libre) con:

1. Un diseño / templates no usados en la clase, con un menú que tenga mínimamente 4 links (opciones de menú)
2. Login / Logout / Registro / Modificación de Usuarios (incluyendo un avatar o foto del usuario logueado)
3. Funcionalidad de CRUD en la aplicación de al menos 4 modelos, con sus correspondientes formularios, habilitados solo para usuarios logueados
4. Un link a una página Acerca de mí, que cuente con datos del alumno

5. Un search que se use como filtro de la información a mostrar (opcional)

6. Incluir un video que muestre la funcionalidad y navegación sobre el sitio construido

7. Casos de Test


Aplicacion elegida:
Concesionaria/Agencia de autos y motos.
*   En el caso de usuarios logueados pueden acceder al listado de autos, motos, empleados y clientes, todos con permiso de ABM. 

*   En el caso de no estar logueados, cualquier puede acceder al listado de Autos y Motos disponibles, pero sin permisos de agregar, editar o remover. Solo pueden Buscar/Filtrar por Marca.

*   Solo usuarios logueados pueden registrar nuevos usuarios. Esto para prevenir que cualquier persona tenga acceso total al sitio. (Ejemplo, solo un usuario de RRHH puede crear nuevos usuarios)

*   Los usuarios pueden cargar su avatar desde http://127.0.0.1:8000/aplicacion/agregar_avatar

*  Menu de Administracion "Admin"
    user: coderhouse    (es Staff)
    Clave: coder-1234

* El video se encuentra en el Menu "Acerca de Mi" a traves de un link a Youtube

* Casos de Test, se encuentran en la raiz del repositorio con el nombre "Casos de Test.xlsx"

Descripcion de Modelos:
1. Auto
    * Atributos: marca, modelo, año, kilometraje
2. Moto
    * Atributos: marca, modelo, año, kilometraje
3.  Empleado
    * Atributos: Nombre, Apellido, email, telefono

4. Cliente
    * Atributos: Nombre, Apellido, email, telefono

5. Avatar


URL principal: http://127.0.0.1:8000/aplicacion

URLS:
    Inicio: http://127.0.0.1:8000/aplicacion
    Autos: http://127.0.0.1:8000/aplicacion/autos
    Motos: http://127.0.0.1:8000/aplicacion/motos
    Empleados: http://127.0.0.1:8000/aplicacion/empleados
    Clientes: http://127.0.0.1:8000/aplicacion/clientes
    Busqueda de Autos: http://127.0.0.1:8000/aplicacion/buscar_autos
    Dar de alta Auto: http://127.0.0.1:8000/aplicacion/create_auto
    Busqueda de Motos: http://127.0.0.1:8000/aplicacion/buscar_motos
    Dar de alta Moto: http://127.0.0.1:8000/aplicacion/create_moto
    Empleados: http://127.0.0.1:8000/aplicacion/empleados
    Dar de alta Empleado: http://127.0.0.1:8000/aplicacion/create_empleado
    Clientes: http://127.0.0.1:8000/aplicacion/clientes
    Dar de alta Cliente: http://127.0.0.1:8000/aplicacion/create_cliente
    Avatar: http://127.0.0.1:8000/aplicacion/agregar_avatar
    Menu de administracion: http://127.0.0.1:8000/admin/
    Acerca de Mi: http://127.0.0.1:8000/aplicacion/aboutme/



    




