# PANADERIA DELICIAS CASERAS

Programa que permite la gestion de una panaderia, administracion de productos y pedidos.


## Descripcion
La panaderia Delicias Caseras desea hacer un sistema que permita a empleados la administracion de productos y pedidos, y a clientes realizar pedidos y pedir informacion sobre productos.
### Gestion de productos
1.Añadir, editar y eliminar productos  
2.Consultar productos por su codigo, nombre o categoria.  
3.Permite a clientes consultar productos dando informacion limitada  
4.Almacena y gestiona productos y existencias de forma dinamica  

### Gestion de pedidos
1.Añadir, editar y eliminar pedidos.  
2.Consultar pedidos por codigo o producto dentro de pedido.  
3.Permite a los empleados consultar y editar pedidos.  
4.Elimina de existencias los productos pedidos.  
5.Retorna las existencias de los productos no elegidos al editar un pedido  

### Seguridad
1.Solicita una contraseña si se desea ingresar al apartado de empleados, con el fin de evitar que alguien externo a la empresa haga modificaciones sustanciales a los datos del almacenamiento  
2.En caso de que se introduzca una contraseña incorrecta tres veces, se bloquea la terminal y debera ser desbloqueada por un administrador con la contraseña  
3.Si el usuario ingresa la contraseña del administrador de forma erronea tres veces, se bloquea la terminal de forma temporal, dando una nueva oportunidad pasado el tiempo y bloqueandola por mas tiempo en cada intento  
4.La terminal permanecerà bloqueada aun si se reinicia el programa, solo puede ser cambiado su estado ingresando la contraseña del administrador  

## Requisitos previos

-Python

## Instalacion del proyecto

1.Descargar el repositorio: https://github.com/Andre07g/panaderia  

2.Extraer el archivo  

3.Abrir el archivo con un programa de lectura que permita su ejecucion en python  

## Uso del proyecto

El programa esta probado contra errores comunes como errores de tipo valor, se puede usar de forma libre  

## Autores y creditos

Edgar Leal  
https://github.com/Andre07g  

## Contacto

eleal087@gmail.com
