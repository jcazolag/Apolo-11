import os

def limpiar_consola():
    os.system("cls")
def menu_ppal():
    print("*** APOLO 11 - SIMULADOR ***") # Decorador de Título
    print("1. Generar Archivos")
    print("2. Generar Reportes")
    print("3. Ayuda")
    print("4. Salir")
    opc_ppal = input(">>> ").strip(" ")
    
    # Verificar si ya hay archivos preexistentes.
    arch_prev = False # Cambiar False por la comprobación de existencia de archivos
    
    match opc_ppal:
        case "1":
            if arch_prev:
                # Generar menú con archivos preexistentes
                # limpiar_consola()
                menu_arch_pre_true()
            else:
                # Generar menú sin archivos preexistentes
                # limpiar_consola()
                menu_arch_pre_false()
        case "2":
            if arch_prev:
                # Generar menú de reportes con archivos preexistentes
                pass
            else:
                print("No existen archivos para generar el reporte. \n\n")
                menu_ppal()
                pass
        case "3":
            # Mostrar documentación o ReadME file
            pass
        case "4":
            limpiar_consola()
            exit()

def menu_arch_pre_true():
    # Menú cuando se encuentran archivos preexistentes.
    print(f"Existen (X_cantidad_archivos) archivos creados. ¿Qué desea hacer?")
    print("1. Guardar archivos")
    print("2. Eliminar archivos")
    print("3. Volver al menú principal")
    opc_arch_pre_true = input(">>> ")
    match opc_arch_pre_true:
        case "1":
            # Envia los archivos a una carpeta de historial
            print(f"Los archivos se han guardado en la carpeta de historial")
            # Ejecutar menu sin archivos preexistentes
            menu_arch_pre_false()
        case "2":
            # Elimina los archivos preexistentes
            print(f"Se han eliminado (X_cantidad_archivos) archivos")
            # Ejecutar menu sin archivos preexistentes
            menu_arch_pre_false()
        case "3":
            #Vuelve al menú principal:
            menu_ppal()

def menu_arch_pre_false():
    # Menú cuando no se encuentran archivos preexistentes.
    print("1. Generar una cantidad exacta de archivos.")
    print("2. Generar una cantidad aleatoria de archivos.")
    print("3. Volver al menú principal")
    opc_arch_pre_false = input(">>> ")
    match opc_arch_pre_false:
        case "1":
            # Genera una cantidad exacta de archivos
            num_archivos = input("Introduzca la cantidad de archivos a generar: ")
            # Ejecutar script para crear los archivos.
            # Mostrar barra de progreso
            # Ejecutar menú de generador de reportes
            pass
        case "2":
            # Ejecutar menu para generar una cantidad aleatoria de archivos
            menu_arch_random()
        case "3":
            # Vuelve al menú principal:
            menu_ppal()

def menu_arch_random():
    # Menú para generar una cantidad aleatoria de archivos
    print("1. Definir rango de aleatoriedad")
    print("2. Generar cantidad aleatoria de archivos")
    print("3. Volver al menú anterior")
    opc_arch_random = input(">>> ")
    match opc_arch_random:
        case "1":
            min = int(input("Ingrese mínimo de archivos: "))
            max = int(input("Ingrese máximo de archivos: "))
            # Ejecutar script para crear los archivos con rango de aleatoriedad.
            pass
        case "2":
            # Ejecutar script para crear archivos aleatoriamente
            pass
        case "3":
            # Volver al menú anterior
            menu_arch_pre_false()

menu_ciclo = True
while menu_ciclo:
    menu_ppal()


