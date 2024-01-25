import os
import random
import generador.generador_archivos as ga
import generador.generador_informes as gi
from simulador.simulador import Apolo11Simulador
from utilidades.archivos import ArchivosUtil
from utilidades.presentacion import PresentacionUtil


class MenuUtil:

    def __init__(self) -> None:
        self.ruta_archivos: str = os.path.join(os.getcwd(), "files")
        self.ruta_devices: str = os.path.join(self.ruta_archivos, "devices")
        self.apolo11_simulador = Apolo11Simulador(self.ruta_archivos)
        self.archivos_existentes = ArchivosUtil.files_search(".log", self.ruta_devices)
        self.generador_informes = gi.GeneradorInformes(self.ruta_devices)
        self.generador_archivos = ga.GeneradorArchivos(self.ruta_devices)
        pass


    def menu_ppal(self) -> None:
        print("\nElija una de las siguiente opciones: ", end="\n")
        print("1. Generar Archivos")
        print("2. Generar Reportes")
        print("3. Ayuda")
        print("4. Salir", end="\n\n")
        opc_ppal = input(">>> ").strip(" ")
        self.menu_func(opc_ppal)


    def menu_func(self, opcion: str) -> None:
        self.archivos_existentes = ArchivosUtil.files_search(".log", self.ruta_devices)
        match opcion:
            case "1":
                if (self.archivos_existentes):
                    self.menu_existen_archivos(len(self.archivos_existentes))
                else:
                    PresentacionUtil.limpiar_consola()
                    print("\n\nElija una de las siguiente opciones: ", end="\n")
                    print("1. Generar una cantidad exacta de archivos")
                    print("2. Generar una cantidad aleatoria de archivos")
                    print("3. Volver al menú principal", end="\n\n")
                    opc_arch = input(">>> ")
                    match opc_arch:
                        case "1":
                            numero_archivos = int(input("Introduzca la cantidad de archivos a generar: "))
                            self.generador_archivos.generar(numero_archivos)
                            PresentacionUtil.limpiar_consola()
                            print(f"\n\nSe generaron {numero_archivos} archivos exitosamente")
                            self.menu_ppal()
                        case "2":
                            self.menu_aleatoriedad()
                        case "3":
                            PresentacionUtil.limpiar_consola()
                            self.menu_ppal()
            case "2":
                if self.archivos_existentes:
                    self.generador_informes.generar()
                    pass
                else:
                    print("No existen archivos para generar el reporte. \n\n")
                    PresentacionUtil.limpiar_consola()
                    MenuUtil.menu_ppal()
            case "3":
                PresentacionUtil.limpiar_consola()
                os.system("python Apolo-11.py -h")
            case "4":
                PresentacionUtil.limpiar_consola()
                exit()


    def menu_existen_archivos(self, cantidad_archvos: int) -> None:
        PresentacionUtil.limpiar_consola()
        print(f"\n\nATENCIÓN: Se encontraron {cantidad_archvos} archivos ya existentes", end="\n\n")
        print("Elija una de las siguientes opciones para continuar:", end="\n")
        print("1. Generar reporte de los archivos existentes y moverlos a backups")
        print("2. Eliminar los archivos")
        print("3. Cancelar y salir", end="\n\n")
        opcion = input(">>> ")
        
        match opcion:
            case "1": 
                generador_informe = gi.GeneradorInformes(self.ruta_devices)
                generador_informe.generar()
            case "2": 
                ArchivosUtil.file_remove(".log", self.ruta_devices)
                self.menu_ppal()
            case "3":
                print("\nSimulación finalizada", end="\n\n")
                PresentacionUtil.limpiar_consola()


    def menu_aleatoriedad(self):
        print("\n1. Definir rango de aleatoriedad")
        print("2. Generar cantidad aleatoria de archivos")
        print("3. Volver al menú anterior", end="\n\n")
        opc_arch_random = input(">>> ")
        match opc_arch_random:
            case "1":
                min = int(input("\nIngrese mínimo de archivos: "))
                max = int(input("Ingrese máximo de archivos: "))
                if (max > min):
                    numero_archivos = random.randint(min, max)
                    self.generador_archivos.generar(numero_archivos)
                    PresentacionUtil.limpiar_consola()
                    print(f"\n\nSe generaron {numero_archivos} archivos exitosamente")
                    self.menu_ppal()
                else:
                    print("\nATENCIÓN: El mínimo de archivos no puede ser mayor que el máximo de archivos")
                    self.menu_ppal()
            case "2":
                numero_archivos = random.randint(0, 100)
                self.generador_archivos.generar(numero_archivos)
                PresentacionUtil.limpiar_consola()
                print(f"\n\nSe generaron {numero_archivos} archivos exitosamente")
                self.menu_ppal()
            case "3":
                PresentacionUtil.limpiar_consola()
                self.menu_ppal()
