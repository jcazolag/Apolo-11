import os
import random
import generador.generador_archivos as ga
import generador.generador_informes as gi
import utilidades.util as util

class Apolo11Simulador:
    
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia
        self.ruta_devices = os.path.join(self.ruta_preferencia, "devices")
        self.ruta_backups = os.path.join(self.ruta_preferencia, "backups")
        util.validar_path(self.ruta_devices)
        util.validar_path(self.ruta_backups)

    def ejecutar_simulacion(self, intervalo=20, num_archivos=random.randint(1, 100)):
        try:
            print("\nMISION APOLO-11", end="\n\n")

            # Valida si ya hay archivos existentes
            validar_archivos = util.files_search(".log", self.ruta_devices) 
            if validar_archivos is None:
                generador_archivos = ga.GeneradorArchivos(self.ruta_devices)
                generador_archivos.generar(num_archivos)
            else:
                bucle = True
                print(f"Se encontraron {len(validar_archivos)} archivos ya existentes", end="\n\n")
                
                while bucle:
                    print("Elija una de las siguientes opciones para seguir:\n\n - 1. Generar informe de los archivos existentes y moverlos a backups\n - 2. Eliminar los archivos\n - 3. Cancelar y salir\n\n")
                    opcion = input(">>>")
                    
                    if opcion.strip(" ") == "1":
                        print("opcion 1")
                        generador_informe = gi.GeneradorInformes(self.ruta_devices)
                        generador_informe.generar()
                        bucle = False
                    elif opcion.strip(" ") == "2":
                        util.file_remove(".log", self.ruta_devices)
                        bucle = False
                    elif opcion.strip(" ") == "3":
                        print("\nSimulacion finalizada\n")
                        bucle = False
                        break
                    else:
                        print("\nOpción incorrecta. Intentelo nuevamente", end="\n\n")
        except Exception as error:
            print("An error occurred:", type(error).__name__, "-", error)