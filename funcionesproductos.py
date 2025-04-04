import json
from menues import *
global productosjson
productosjson="inventario.json"

def leerinvjson():
     with open (productosjson,"r") as file:
        productos=json.load(file)
     return productos
productos=leerinvjson()  

def prodcase():
    while True:
        op=gestion_prod()
        match op:
            case "1":
                limpiar_consola()
                añadir_producto()
            case "2":
                limpiar_consola()
                editar_producto()
            case "3":
               limpiar_consola()
               eliminar_productos()
               time.sleep(1)
               limpiar_consola()
            case "4":
                print("Volviendo al menu anterior...")
                time.sleep(1)
                limpiar_consola()
                break
            case _: 
                print("Digite una opcion valida")

def añadir_producto():
        global productosjson
        productos=leerinvjson()
        codigo=input("Ingrese el codigo del producto: ")
        existe=False
        for x in productos:
            for codige in x.values():
                if codige==codigo:      
                    existe=True         
        if existe==True:
             print("El codigo de producto ya està registrado...")
             time.sleep(2)
             limpiar_consola()
        else:             
            nombre=input("Ingrese el nombre: ")
            categoria=input("Ingrese la categoria: ")
            descripcion=input("Ingrese la descripcion: ")
            proveedor=input("Ingrese el provedor: ")
            while True:
               try:
                    cant_stock=int(input("Ingrese las existencias: "))
                    break
               except: print("Error, ingrese una cantidad valida")
            while True:
                  try:
                    precioventa=int(input("Ingrese el precio de venta: "))
                    break
                  except: print("Error, ingrese una cantidad valida")
            while True:
                  try:
                    preciocompra=int(input("Ingrese el precio de compra: "))
                    break
                  except: print("Error, ingrese una cantidad valida")
            nuevoprod={    "Codigo": codigo,
                            "Nombre": nombre,
                            "Categoria": categoria,
                            "Descripcion": descripcion,
                            "Proveedor": proveedor,
                            "Existencias": cant_stock,
                            "Precio de venta": precioventa,
                            "Precio de compra": preciocompra}
            productos.append(nuevoprod)
            with open (productosjson,"w") as file:
                json.dump(productos, file, indent=4)
            print("El producto se registro exitosamente")
            time.sleep(2)
            limpiar_consola()

def editar_producto():
    limpiar_consola()
    global productosjson
    existencia=False
    productos=leerinvjson()
    codigo=input("Ingrese el codigo del producto: ")
    for producto in productos:
         for valor in producto.values():
              if valor==codigo:
                   indice=productos.index(producto)
                   existencia=True
    if existencia==True:
            nombre=input("Ingrese el nombre: ")
            categoria=input("Ingrese la categoria: ")
            descripcion=input("Ingrese la descripcion: ")
            proveedor=input("Ingrese el provedor: ")
            cant_stock=int(input("Ingrese las existencias: "))
            precioventa=int(input("Ingrese el precio de venta: "))
            preciocompra=int(input("Ingrese el precio de compra: "))
            productos[indice]={    "Codigo": codigo,
                            "Nombre": nombre,
                            "Categoria": categoria,
                            "Descripcion": descripcion,
                            "Proveedor": proveedor,
                            "Existencias": cant_stock,
                            "Precio de venta": precioventa,
                            "Precio de compra": preciocompra}
            with open (productosjson,"w") as file:
                json.dump(productos, file, indent=4)
            print("El producto se editò exitosamente")
    else: 
         print("El producto no està registrado\n¿Desea registrarlo?")
         op=input("1.Si\n2.No\nDigite su opcion: ")
         match op:
              case "1":  
                    añadir_producto()
                    time.sleep(1)
                    limpiar_consola()
               
              case "2": 
                    print("Volviendo al menù anterior...")
                    time.sleep(1)
                    limpiar_consola()
              case _: print("Opciòn no valida, volviendo al menu anterior")
                             
def eliminar_productos():
    global productosjson
    borrado=0
    productos=leerinvjson()
    codigo=input("Ingrese el codigo del producto: ")
    for producto in productos:
         if producto["Codigo"]==codigo:
                   advertencia=input("¿Esta seguro de que desea eliminar el producto?\n1.Si\n2.No\nDigite: ")
                   while True:
                    if advertencia=="1":
                         limpiar_consola()
                         indice=productos.index(producto)
                         del productos[indice]
                         print("Se ha eliminado correctamente")
                         time.sleep(1)
                         limpiar_consola()
                         borrado=True
                         break
                    elif advertencia=="2":
                              print("Cancelando operaciòn...")
                              time.sleep(1)
                              borrado=True
                              limpiar_consola()
                              break
                    else: print("Ingrese una opciòn valida")
    if borrado==False:
        print("El producto ingresado no existe")   
        time.sleep(1)
        limpiar_consola()            
    with open("inventario.json","w")as file:
         json.dump(productos, file, indent=4)

def consulta_inventario():
     print("Los productos en base de datos son: ")
     for producto in productos:
          print("------------")
          for clave, valor in producto.items():
               print(f"{clave}->{valor}")
          if producto["Existencias"]<20:
                                    print("⚠️  El producto esta a punto de agotarse...  ⚠️")
          print("------------")

def inventarioempleados():
     while True:
          op=inventarios_menu()
          match op:
               case "1":
                    limpiar_consola()
                    consulta_inventario()
                    input("Presione cualquier tecla para continuar")
               case "2":
                    limpiar_consola()
                    verago_disp()
                    input("Presione cualquier tecla para continuar")
               case "3":
                    limpiar_consola()
                    prodxcodigo()
                    input("Presione cualquier tecla para continuar")
               case "4":
                    limpiar_consola()
                    proxnombre()
                    input("Presione cualquier tecla para continuar")
               case "5":
                    limpiar_consola()
                    proxcategoria()
                    input("Presione cualquier tecla para continuar")
               case "6":
                    print("Volviendo al menu anterior...")
                    time.sleep(1)
                    limpiar_consola()
                    break
               case _:print("Ingrese una opciòn valida: ")
          time.sleep(1)
          limpiar_consola()

def verago_disp():
     while True:
          op=input("1.Disponibles\n2.Agotados\n3.A punto de agotarse\n4.Volver al menu anterior\nDigite: ")
          match op:
               case "1":
                    print("Los productos disponibles son: ")
                    for producto in productos:
                         if producto["Existencias"]>0:
                              print("------------")
                              for clave, valor in producto.items():
                                   print(f"{clave}->{valor}")
                              if producto["Existencias"]<20:
                                    print("⚠️  El producto esta a punto de agotarse...  ⚠️")
                              print("------------")
               case "2":
                    print("Los productos agotados son: ")
                    for producto in productos:
                         if producto["Existencias"]==0:
                              print("------------")
                              for clave, valor in producto.items():
                                   print(f"{clave}->{valor}")
                              print("------------")
               case "3":
                    print("Los productos son: ")
                    for producto in productos:
                         if producto["Existencias"]<20:
                              print("------------")
                              for clave, valor in producto.items():
                                   print(f"{clave}->{valor}")
                              print("------------")
               case "4":
                      print("Volviendo al menu anterior...")
                      break          
               case _: print("Ingrese una opciòn valida")

def prodxcodigo():
          codiexiste=False
          code=input("Ingresa el codigo: ")
          for producto in productos:
               if producto["Codigo"]==code:
                    codiexiste=True
                    print("------------")
                    for clave, valor in producto.items():
                                   print(f"{clave}->{valor}")
                    if producto["Existencias"]<20:
                                    print("⚠️  El producto esta a punto de agotarse...  ⚠️")
                    print("------------")
          if codiexiste==False: print("El producto no existe")

def proxnombre():
          codiexiste=False
          nome=input("Ingresa el nombre: ")
          for producto in productos:
               if producto["Nombre"]==nome:
                    codiexiste=True
                    print("------------")
                    for clave, valor in producto.items():
                                   print(f"{clave}->{valor}")
                    if producto["Existencias"]<20:
                                    print("⚠️  El producto esta a punto de agotarse...  ⚠️")
                    print("------------")
          if codiexiste==False: print("El producto no existe")

def proxcategoria():
          codiexiste=False
          categori=input("Ingresa la categoria: ")
          for producto in productos:
               if producto["Categoria"]==categori:
                    codiexiste=True
                    print("------------")
                    for clave, valor in producto.items():
                                   print(f"{clave}->{valor}")
               if producto["Existencias"]<20:
                                    print("⚠️  El producto esta a punto de agotarse...  ⚠️")
          print("------------")
          if codiexiste==False: print("El producto no existe")

def consultaclien():
     while True:
          op=clien_product()
          match op:
               case "1":
                    cliennom()
               case "2":
                    cliencat()
               case "3":
                    limpiar_consola()
                    clientdisp()
               case "4":
                    print("Volviendo al menu anterior...")
                    time.sleep(1)
                    break
               case _:print("Ingrese una opciòn valida")

def cliennom():
          codiexiste=False
          nome=input("Ingresa el nombre: ")
          limpiar_consola()
          for producto in productos:
               if producto["Nombre"]==nome:
                    codiexiste=True
                    print("------------")
                    for clave, valor in producto.items():
                                   if clave=="Codigo":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Nombre":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Categoria":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Descripcion":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Precio de venta":
                                        print(f"{clave}->{valor}")
                                   else:()
                    print("------------")
          if codiexiste==False: print("El producto no existe")
          input("Presione cualquier tecla para volver")
          time.sleep(1)
          limpiar_consola()

def cliencat():
          codiexiste=False
          nome=input("Ingresa la categoria: ")
          limpiar_consola()
          for producto in productos:
               if producto["Categoria"]==nome:
                    codiexiste=True
                    print("------------")
                    for clave, valor in producto.items():
                                   if clave=="Codigo":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Nombre":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Categoria":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Descripcion":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Precio de venta":
                                        print(f"{clave}->{valor}")
                                   else:()
                    print("------------")
          if codiexiste==False: print("La categoria o productos no existen no existe")
          input("Presione cualquier tecla para volver")
          time.sleep(1)
          limpiar_consola()

def clientdisp():
          for producto in productos:
               if producto["Existencias"]>0:
                    codiexiste=True
                    print("------------")
                    for clave, valor in producto.items():
                                   if clave=="Codigo":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Nombre":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Categoria":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Descripcion":
                                        print(f"{clave}->{valor}")
                                   elif clave=="Precio de venta":
                                        print(f"{clave}->{valor}")
                                   else:()
                    print("------------")
          input("Presione cualquier tecla para volver")
          time.sleep(1)

def advertenciaproductosagotar():
      productos=leerinvjson()
      print("⚠️ Advertencia ⚠️")
      print("Los siguientes productos estan por agotarse:")
      for producto in productos:
            if producto["Existencias"]<20 and producto["Existencias"]>0:
                  print(f"{producto['Nombre']}->{producto['Existencias']}")

