from menues import *
from funcionesproductos import *
from funcionespedidos import *
import json
import time
import os
clavepanaderia="superpan"
claveadmin="pan123"
intentos=3
salidamen=False
intentosadmin=3
tiempe=10
saludo()
time.sleep(1)
limpiar_consola()
block="bloqueado.json"
with open (block, "r") as file:
    bloque=json.load(file)
bloqueado=bloque["bloqueado"]
while True:
    block="bloqueado.json"
    with open (block, "r") as file:
        bloque=json.load(file)
    bloqueado=bloque["bloqueado"]
    if bloqueado==False:
        while True:
            op=mostrar_menu()
            limpiar_consola()
            match op:
                case "1":
                    print("PERFIL: EMPLEADOS    ")
                    clave=input("Ingrese la contraseña: ")
                    if clave==clavepanaderia:
                        intentos=3
                        print("Contraseña correcta")
                        time.sleep(1)
                        limpiar_consola()
                        advertenciaproductosagotar()
                        input("Presione cualquier tecla para continuar")
                        limpiar_consola()
                        while True:
                            limpiar_consola()
                            op=sub_prod()   
                            match op:
                                case "1":
                                    limpiar_consola()
                                    prodcase()
                                case "2":
                                    limpiar_consola()
                                    while True:
                                        op=opcion_pedidos()
                                        if op=="1":
                                            limpiar_consola()
                                            añadir_pedidos()
                                        elif op=="2":
                                            limpiar_consola()
                                            editar_pedido()
                                            time.sleep(1)
                                            limpiar_consola()
                                        elif op=="3":
                                            limpiar_consola()
                                            eliminar_pedido()
                                            limpiar_consola()
                                        elif op=="4":
                                            while True:
                                                limpiar_consola()
                                                op=menupedidosemple()
                                                if op=="1":
                                                    limpiar_consola()
                                                    buscarpedcodped()
                                                    limpiar_consola()
                                                elif op=="2":
                                                    limpiar_consola()
                                                    buscarpedcod()
                                                    limpiar_consola()
                                                elif op=="3":
                                                    limpiar_consola()
                                                    buscarpednom()
                                                    limpiar_consola()
                                                elif op=="4":
                                                    limpiar_consola()
                                                    buscarpedclie()
                                                    limpiar_consola()
                                                elif op=="5":
                                                    print("Volviendo al menu anterior...")
                                                    time.sleep(1)
                                                    limpiar_consola()
                                                    break
                                        elif op=="5":
                                            print("Volviendo al menù anterior...")
                                            time.sleep(1)
                                            limpiar_consola()
                                            break
                                        else:
                                            print("Ingrese una opciòn valida")
                                            limpiar_consola()
                                        
                                case "3":
                                    limpiar_consola()
                                    inventarioempleados()
                                case "4":
                                    print("Cerrando sesion...")
                                    time.sleep(1)
                                    limpiar_consola()
                                    break
                                case _: 
                                    print("Ingrese una opciòn valida: ")
                                    limpiar_consola()
                    else:  
                        intentos-=1
                        limpiar_consola()
                        print(f"Clave incorrecta\nQuedan {intentos} intentos")
                    if intentos<=0:
                            bloque["bloqueado"]=True
                            with open(block, "w") as file:
                                json.dump(bloque,file)
                            print("********************************************************")
                            print("-----Terminal bloqueada, contacte a un administrador-----")
                            time.sleep(3)
                            limpiar_consola()
                            break
                case "2":   
                     while True:
                        limpiar_consola()
                        op=menu_clientes()
                        match op:
                            case "1":
                                limpiar_consola()
                                añadir_pedidos()
                                input("Presione cualquier tecla para volver")
                                limpiar_consola()
                            case "2":
                                limpiar_consola()
                                consultaclien()
                                limpiar_consola()
                            case "3":
                                print("Volviendo al menu anterior...")
                                time.sleep(1)
                                limpiar_consola()
                                break
                            case _: 
                                print("Ingrese una opciòn valida")
                                limpiar_consola()
                case "3":
                    print("Saliendo")
                    time.sleep(2)
                    limpiar_consola()
                    salidamen=True
                    break
                case _:
                    print("Ingrese una opciòn valida")
                    limpiar_consola()
        if salidamen==True:
                    despedida()
                    break
    else: 
        print("********************************************************")
        print("             El terminal esta bloqueado")
        print("********************************************************")
        contradmin=input("Ingrese la contraseña del administrador: ")
        if contradmin==claveadmin:
            print(" Acceso correcto, inicializando sistema...")
            time.sleep(2)
            limpiar_consola()
            bloque["bloqueado"]=False
            intento=3
            intentosadmin=3
            with open (block, "w") as file:
                json.dump(bloque, file)
        else: 
            intentosadmin-=1
            print(f"Contraseña incorrecta\nQuedan {intentosadmin} intentos...")
            time.sleep(2)
            limpiar_consola()
    if intentosadmin==0:
            print(f"Intentos agotados, intente nuevamente en {tiempe} segundos")
            time.sleep(tiempe)
            intentosadmin=1
            tiempe+=20
            limpiar_consola()



