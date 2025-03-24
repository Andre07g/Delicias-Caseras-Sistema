import time
import os

def mostrar_menu():
    men="""
    *******Menu Principal********
    1.Para empleados
    2.Para clientes
    3.Salir
    """
    print(men)
    return input("Ingrese una opciòn: ")

def sub_prod():
     supr="""
     ****Opciones Empleado****
     1.Gestionar productos
     2.Gestionar pedidos
     3.Consulta de inventarios
     4.Cerrar sesion
     """
     print(supr)
     return input("Seleccione una opcion: ")

def gestion_prod():
    gestion="""
    ****Gestionar Productos****
    1.Añadir productos
    2.Editar productos
    3.Eliminar productos
    4.Volver al menu anterior
    """
    print(gestion)
    return input("Ingrese una opciòn: ")

def opcion_pedidos():
    menupedidos="""
    ****Gestionar Pedidos****
    1.Añadir pedidos
    2.Editar pedidos
    3.Eliminar pedidos
    4.Buscar pedidos
    5.Volver al menu anterior
    """
    print(menupedidos)
    return input("Ingrese una opciòn: ")

def inventarios_menu():
          menuinventarios="""
          *********Inventarios*********
          1.Ver todos los productos
          2.Ver productos disponibles/agotados
          3.Buscar producto por codigo
          4.Buscar producto por nombre
          5.Buscar producto por categoria
          6.Volver al menù anterior
          """
          print(menuinventarios)
          return input("Ingrese una opciòn: ")

def menu_clientes():
    menucl="""
    *****CLIENTES*****
    1.Realizar un pedido
    2.Consultar producto
    3.Volver al menu anterior
    """
    print(menucl)
    return input("Ingrese una opciòn: ")

def clien_product():
    prodcli="""
    ********Productos**********
    1.Buscar por nombre
    2.Buscar por categoria
    3.Ver disponibles
    4.Volver al menu anterior"""
    print(prodcli)
    return input("Ingrese una opciòn: ")

def saludo():
    print("=" * 50)
    print("🍞 ¡Bienvenido a Panadería Delicias Caseras! 🥖".center(50))
    print("=" * 50)
    print("\nCargando sistema, por favor espere...\n")
    time.sleep(2)
    print("Sistema listo. ¡Que tengas un buen día!\n")

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def despedida():
    print("=" * 50)
    print("🍞 ¡Gracias por preferirnos, que tengas buen dia! 🥖".center(50))
    print("=" * 50)
    time.sleep(2)

def menupedidosemple():
    menupedido="""
        **********Pedidos**********
        1.Buscar por codigo
        2.Buscar por  codigo del producto incluido
        3.Buscar por nombre del producto incluido
        4.Buscar por codigo de cliente
        5.Volver al menu anterior
        """
    print(menupedido)
    return input("Ingrese una opción: ")