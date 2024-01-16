import os
import random
from dependencies.simulador import Apolo11Simulador
import dependencies.project_utils as pu

def menu_ppal():
    # Obtiene la ruta donde se guardan los archivos
    ruta_preferencia = os.path.join(os.getcwd(), "files")
    pu.ValidarPath(ruta_preferencia)

    # Inicializa el objeto del simulador y se le añade la ruta de guardado de archivos
    apolo11_simulador = Apolo11Simulador(ruta_preferencia)
    
    print("*** APOLO 11 - SIMULADOR ***") # Decorador de Título
    print("1. Generar Archivos")
    print("2. Generar Reportes")
    print("3. Ayuda")
    print("4. Salir")
    opc_ppal = input(">>> ").strip(" ")
    
    arch_prev = True
    
    match opc_ppal:
        case "1":
                # pu.limpiar_consola()
                # Menú cuando no se encuentran archivos preexistentes.
                print("1. Generar una cantidad exacta de archivos.")
                print("2. Generar una cantidad aleatoria de archivos.")
                print("3. Volver al menú principal")
                opc_arch = input(">>> ")
                match opc_arch:
                    case "1":
                        # Genera una cantidad exacta de archivos
                        numero_archivos = int(input("Introduzca la cantidad de archivos a generar: "))
                        apolo11_simulador.ejecutar_simulacion(num_archivos=numero_archivos)
                        return numero_archivos
                    case "2":
                        # Menú para generar una cantidad aleatoria de archivos
                        print("1. Definir rango de aleatoriedad")
                        print("2. Generar cantidad aleatoria de archivos")
                        print("3. Volver al menú anterior")
                        opc_arch_random = input(">>> ")
                        match opc_arch_random:
                            case "1":
                                min = int(input("Ingrese mínimo de archivos: "))
                                max = int(input("Ingrese máximo de archivos: "))
                                numero_archivos = random.randint(min, max)
                                apolo11_simulador.ejecutar_simulacion(num_archivos=numero_archivos)
                                return numero_archivos
                            case "2":
                                numero_archivos = random.randint(0, 100)
                                apolo11_simulador.ejecutar_simulacion(num_archivos=numero_archivos)
                                return numero_archivos
                            case "3":
                                # Volver al menú anterior
                                pass
        case "2":
            if arch_prev:
                # Generar menú de reportes con archivos preexistentes
                pass
            else:
                print("No existen archivos para generar el reporte. \n\n")
                menu_ppal()
        case "3":
            # Mostrar documentación o ReadME file
            pass
        case "4":
            pu.limpiar_consola()
            exit()


