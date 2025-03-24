
from funcionesproductos import leerinvjson, añadir_producto, clientdisp
from menues import limpiar_consola
import json, time
from datetime import datetime
pedidosjson="pedidos.json"
productosjson="inventario.json"

def leerpedjson():
     with open (pedidosjson,"r") as file:
        pedidos=json.load(file)
     return pedidos

def añadir_pedidos():
        global pedidosjson, productosjson
        hoy=str(datetime.today().date())
        pedidos=leerpedjson()
        productos=leerinvjson()
        codigo=input("Ingrese el codigo del pedido: ")
        existe=False
        for x in pedidos:
            for codige in x.values():
                if codige==codigo:      
                    existe=True         
        if existe==True:
             print("Ya existe un pedido con este codigo")
             time.sleep(2)
             limpiar_consola()

        else:             
            codigocliente=input("Ingrese el codigo del cliente: ") 
            prodpedidos=[]
            preciototal=0
            numerolinea=1
            while True:
                 op=input("1.Para añadir producto\n2.Para terminar pedido\nIngrese su opciòn: ")
                 match op:
                      case "1":
                           clientdisp()
                           codigoprod=input("Ingrese codigo del producto: ")
                           indice=None
                           for i, producto in enumerate(productos):
                                   if producto["Codigo"] == codigoprod:
                                         indice=i
                                         
                           if indice is not None:
                                        limpiar_consola()
                                        print(f"{productos[indice]["Nombre"]} restantes->{productos[indice]["Existencias"]}")
                                        print(f"Precio->{productos[indice]["Precio de venta"]}")
                                        while True:
                                            while True:
                                                try:
                                                    cantidad=int(input("Ingrese cantidad a comprar: "))
                                                    break
                                                except: print("Error, ingrese una cantidad valida") 
                                            if cantidad>0:
                                                if cantidad>productos[indice]["Existencias"]: print("No hay suficientes existencias")
                                                else: 
                                                       op=input("1.Para confirmar\n2.Para cancelar\nDigite: ")
                                                       if op=="1": 
                                                            productos[indice]["Existencias"]-=cantidad
                                                            print("Añadido al carrito correctamente")
                                                            limpiar_consola()
                                                            prodpedidos.append({"numero_linea":numerolinea,"codigoproducto":codigoprod,"nombre":productos[indice]["Nombre"],"cantidad":cantidad,"precio_unidad":productos[indice]["Precio de venta"]})
                                                            numerolinea+=1
                                                            preciototal+=cantidad*productos[indice-1]["Precio de venta"]
                                                            with open (productosjson,"w") as file:
                                                                    json.dump(productos, file, indent=4)
                                                            break    
                                                       else: 
                                                            break
                                            else:
                                                 print("Ingrese una cantidad valida")
                                                 break 
                           else: print("El producto no existe") 
                           limpiar_consola()

                      case "2":
                           limpiar_consola()
                           nuevopedido={"codigo_pedido":codigo,
                                        "codigo_cliente":codigocliente,
                                        "fecha_pedido":hoy,
                                        "detalles_pedido":prodpedidos
                                        }                  
                           print("**********************************")
                           for clavee, valore in nuevopedido.items():
                                 if clavee=="codigo_pedido":
                                       print(f"Codigo del pedido:{valore}")
                                 elif clavee=="codigo_cliente":
                                       print(f"Codigo del cliente:{valore}")
                                 elif clavee=="fecha_pedido":
                                       print(f"Fecha del pedido:{valore}")
                                 elif clavee=="detalles_pedido":
                                       print(f"---Detalles del pedido---")
                                       for dato in valore:
                                             for clave, valor in dato.items():
                                                  if clave=="numero_linea":
                                                        print(f"#{valor}",end="")
                                                  elif clave=="nombre":
                                                         print(f"{valor}/",end="")
                                                  elif clave=="cantidad":
                                                        print(f"Cantidad->{valor}/",end="")
                                                  elif clave=="precio_unidad":
                                                        print(f"Precio->{valor}")
                                       print("------------------------")
                                 
                           print(f"El precio total del pedido son: {preciototal}")
                           print("********************************")                 
                           pedidos=leerpedjson()
                           pedidos.append(nuevopedido)
                           with open(pedidosjson,"w") as file:
                                json.dump(pedidos, file, indent=4)
                           print("Pedido registrado exitosamente")
                           input("Presione cualquier tecla para volver")
                           limpiar_consola()
                           break
                      case _:
                           print("Ingrese una opciòn valida")

def editar_pedido():
    global productosjson, pedidosjson
    hoy=str(datetime.today().date())
    productos=leerinvjson()
    pedidos=leerpedjson()
    pedidoexiste=False
    codigo_pedido = input("Ingrese el código del pedido: ")
    for pedido in pedidos:
          if pedido.get("codigo_pedido") == codigo_pedido:
               pedidoexiste=True
               indisex=pedidos.index(pedido)
               for detalle in pedido.get("detalles_pedido", []): 
                    codigoproducto = detalle.get("codigoproducto")
                    cantidad = detalle.get("cantidad", 0)
                    for producto in productos:
                         if producto.get("Codigo") == codigoproducto:
                              producto["Existencias"] += cantidad
                         with open(productosjson,"w") as file:
                               json.dump(productos, file, indent=4)
    if pedidoexiste==False:
             print("No existe un pedido con este codigo")   
    else:             
            codigocliente=input("Ingrese el codigo del cliente: ") 
            prodpedidos=[]
            preciototal=0
            numerolinea=1
            while True:
                 op=input("1.Para añadir producto\n2.Para terminar pedido\nIngrese su opciòn: ")
                 match op:
                      case "1":
                           codigoprod=input("Ingrese codigo del producto: ")
                           indice=None
                           for i, producto in enumerate(productos):
                                   if producto["Codigo"] == codigoprod:
                                         indice=i
                                         
                           if indice is not None:
                                        print(f"{productos[indice]["Nombre"]} restantes->{productos[indice]["Existencias"]}")
                                        print(f"Precio->{productos[indice]["Precio de venta"]}")
                                        while True:
                                            while True:
                                                try:
                                                    cantidad=int(input("Ingrese cantidad a comprar: "))
                                                    break
                                                except: print("Error, ingrese una cantidad valida")
                                            if cantidad>0:
                                                if cantidad>productos[indice]["Existencias"]: print("No hay suficientes existencias")
                                                else: 
                                                       op=input("1.Para confirmar\n2.Para cancelar\nDigite: ")
                                                       if op=="1": 
                                                            productos[indice]["Existencias"]-=cantidad
                                                            print("Añadido al carrito correctamente")
                                                            prodpedidos.append({"numero_linea":numerolinea,"codigoproducto":codigoprod,"nombre":productos[indice]["Nombre"],"cantidad":cantidad,"precio_unidad":productos[indice]["Precio de venta"]})
                                                            numerolinea+=1
                                                            preciototal+=cantidad*productos[indice-1]["Precio de venta"]
                                                            with open (productosjson,"w") as file:
                                                                    json.dump(productos, file, indent=4)
                                                            break    
                                                       else: 
                                                            break
                                            else:
                                                 print("Ingrese una cantidad valida")
                                                 break 
                           else: print("El producto no existe")               
                      case "2":
                           
                           nuevopedido={"codigo_pedido":codigo_pedido,
                                        "codigo_cliente":codigocliente,
                                        "fecha_pedido":hoy,
                                        "detalles_pedido":prodpedidos
                                        }                  
                           print("**********************************")
                           for clavee, valore in nuevopedido.items():
                                 if clavee=="codigo_pedido":
                                       print(f"Codigo del pedido:{valore}")
                                 elif clavee=="codigo_cliente":
                                       print(f"Codigo del cliente:{valore}")
                                 elif clavee=="fecha_pedido":
                                       print(f"Fecha del pedido:{valore}")
                                 elif clavee=="detalles_pedido":
                                       print(f"---Detalles del pedido---")
                                       for dato in valore:
                                             for clave, valor in dato.items():
                                                  if clave=="numero_linea":
                                                        print(f"#{valor}",end="")
                                                  elif clave=="nombre":
                                                         print(f"{valor}/",end="")
                                                  elif clave=="cantidad":
                                                        print(f"Cantidad->{valor}/",end="")
                                                  elif clave=="precio_unidad":
                                                        print(f"Precio->{valor}")
                                       print("------------------------")
                                 
                           print(f"El precio total del pedido son: {preciototal}")
                           print("********************************")                 
                           pedidos=leerpedjson()
                           pedidos[indisex]=nuevopedido
                           with open(pedidosjson,"w") as file:
                                json.dump(pedidos, file, indent=4)
                           print("Pedido registrado exitosamente")
                      case _:
                           print("Ingrese una opciòn valida")
     
def eliminar_pedido():
    global productosjson, pedidosjson
    productos=leerinvjson()
    pedidos=leerpedjson()
    pedidoexiste=False
    codigo_pedido = input("Ingrese el código del pedido: ")
    for pedido in pedidos:
          if pedido.get("codigo_pedido") == codigo_pedido:
               pedidoexiste=True
               indisex=pedidos.index(pedido)
               pedidos.pop(indisex)
    if pedidoexiste==True:
          with open ("pedidos.json","w") as file:
                json.dump(pedidos, file, indent=4)
          print("Pedido eliminado correctamente")
    if pedidoexiste==False:
         print("El pedido no existe")
                    
def buscarpedcod():
    pedidos = leerpedjson()
    codigoprode = input("Ingrese el código del producto a buscar: ")
    existere = False
    for pedido in pedidos:
        if any(detalle["codigoproducto"] == codigoprode for detalle in pedido["detalles_pedido"]):
            existere = True
            print("\n------------------------")
            print(f"Código del pedido: {pedido['codigo_pedido']}")
            print(f"Código del cliente: {pedido['codigo_cliente']}")
            print(f"Fecha del pedido: {pedido['fecha_pedido']}")
            print(f"---Detalles del pedido---")
            for detalle in pedido["detalles_pedido"]:
                print(f"#{detalle['numero_linea']}/",end="")
                print(f"{detalle['nombre']}/",end="")
                print(f"Cantidad->{detalle['cantidad']}/",end="")
                print(f"Precio->{detalle['precio_unidad']}/")
            print("------------------------")
    if not existere:
        print("No existe un pedido con este producto.")  
    input("Presione cualquier tecla para volver")
    time.sleep(1)
    limpiar_consola()

def buscarpednom():
    pedidos = leerpedjson()
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    existere = False 
    for pedido in pedidos:
        if any(detalle["nombre"] == nombre_producto for detalle in pedido["detalles_pedido"]):
            existere = True
            print("\n------------------------")
            print(f"Código del pedido: {pedido['codigo_pedido']}")
            print(f"Código del cliente: {pedido['codigo_cliente']}")
            print(f"Fecha del pedido: {pedido['fecha_pedido']}")
            print(f"---Detalles del pedido---")
            for detalle in pedido["detalles_pedido"]:
                print(f"#{detalle['numero_linea']}/",end="")
                print(f"{detalle['nombre']}/",end="")
                print(f"Cantidad->{detalle['cantidad']}/",end="")
                print(f"Precio->{detalle['precio_unidad']}/")
            print("------------------------")
    if not existere:
        print("No existe un pedido con este producto.")  
    input("Presione cualquier tecla para volver")
    time.sleep(1)
    limpiar_consola()

def buscarpedclie():
    pedidos = leerpedjson()
    codigo_cliente = input("Ingrese el código del cliente: ")
    existere = False
    for pedido in pedidos:
        if pedido["codigo_cliente"] == codigo_cliente:
            existere = True
            print("\n------------------------")
            print(f"Código del pedido: {pedido['codigo_pedido']}")
            print(f"Código del cliente: {pedido['codigo_cliente']}")
            print(f"Fecha del pedido: {pedido['fecha_pedido']}")
            print(f"---Detalles del pedido---")
            
            for detalle in pedido["detalles_pedido"]:
                print(f"#{detalle['numero_linea']}/",end="")
                print(f"{detalle['nombre']}/",end="")
                print(f"Cantidad->{detalle['cantidad']}/",end="")
                print(f"Precio->{detalle['precio_unidad']}/")
            print("------------------------")
    if not existere:
        print("No existen pedidos para este cliente.")  
    input("Presione cualquier tecla para volver")
    time.sleep(1)
    limpiar_consola()

def buscarpedcodped():
    pedidos = leerpedjson()
    codigo_pedido = input("Ingrese el código del pedido: ")
    existere = False
    for pedido in pedidos:
        if pedido["codigo_pedido"] == codigo_pedido:
            existere = True
            print("\n------------------------")
            print(f"Código del pedido: {pedido['codigo_pedido']}")
            print(f"Código del cliente: {pedido['codigo_cliente']}")
            print(f"Fecha del pedido: {pedido['fecha_pedido']}")
            print(f"---Detalles del pedido---")
            
            for detalle in pedido["detalles_pedido"]:
                print(f"#{detalle['numero_linea']}/",end="")
                print(f"{detalle['nombre']}/",end="")
                print(f"Cantidad->{detalle['cantidad']}/",end="")
                print(f"Precio->{detalle['precio_unidad']}/")
            print("------------------------")
    if not existere:
        print("No existen pedidos para este codigo de pedido.")  
    input("Presione cualquier tecla para volver")
    time.sleep(1)
    limpiar_consola()