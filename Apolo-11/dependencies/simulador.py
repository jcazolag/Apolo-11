import os
import random
from time import sleep
from datetime import datetime
from .generador import *
from .project_utils import *

class Apolo11Simulador:
    
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia
        self.ruta_devices = os.path.join(self.ruta_preferencia, "devices")
        self.ruta_backups = os.path.join(self.ruta_preferencia, "backups")
        self.misiones = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
        self.estados = ["excellent", "good", "warning", "faulty", "killed", "unknown"]
        self.devise_type = ["Satelite", "Ship", "Space suite", "Space vehicle"]
        ValidarPath(self.ruta_devices)
        ValidarPath(self.ruta_backups)

    def ejecutar_simulacion(self, intervalo=20, num_archivos=random.randint(1, 100)):
        # Lógica para la simulación
        try:
            #print(f"Intervalos: {intervalo} segundos")
            #print(f"Archivos: {max_archivos}")

            print("\nMISION APOLO-11", end="\n\n") #Mensaje de inicio

            #Valida si ya hay archivos existentes
            validar_archivos = files_search(".log", self.ruta_devices) 
            if validar_archivos is None:
                self.generar_archivos(num_archivos)
                #self.generar_informes()
            else:
                bucle  = True
                print(f"Se encontraron {len(validar_archivos)} archivos ya existentes", end="\n\n")
                
                while bucle:
                    print("Elija una de las siguientes opciones para seguir:\n\n - 1. Generar informe de los archivos existentes y moverlos a backups\n - 2. Eliminar los archivos\n - 3. Cancelar y salir\n\n")
                    opcion = input(">>>")
                    
                    if opcion.strip(" ") == "1":
                        print("opcion 1")
                        bucle = False
                    elif opcion.strip(" ") == "2":
                        file_remove(".log", self.ruta_devices)
                        bucle = False
                    elif opcion.strip(" ") == "3":
                        print("\nSimulacion finalizada\n\nAdios")
                        bucle = False
                        break
                    else:
                        print("\nOpcion incorrecta. Intentelo nuevamente", end="\n\n")
        except Exception as error:
            print("An error occurred:", type(error).__name__, "-", error)

    def generar_archivos(self, num_archivos):
        # Lógica para la generación de archivos
        try:
            archivo = GenerarArchivo(self.ruta_devices) #Se inicializa el objeto de la clase GenerarArchivo

            #Iteracion de los archivos creado por cada mision
            iteraciones = {
                "ORBONE": 0,
                "CLNM": 0,
                "TMRS": 0,
                "GALXONE": 0,
                "UNKN": 0
            }
            iteracion = 0 # Numero ed iteracion 
            mision = "" # Mision de la simulacion

            print(f"Generando {num_archivos} archivo(s):", end="\n")
            progress_bar(0, num_archivos)
            #Bucle para crear la cantidad de archivos dado por la variable "num_archivos"
            for i in range(1,num_archivos+1):
                sleep(0.1)
                mission=random.choice(self.misiones)
                match mission:
                    case "ORBONE": 
                        iteraciones["ORBONE"] += 1
                        iteracion = iteraciones["ORBONE"]
                    case "CLNM": 
                        iteraciones["CLNM"] += 1
                        iteracion = iteraciones["CLNM"]
                    case "TMRS": 
                        iteraciones["TMRS"] += 1
                        iteracion = iteraciones["TMRS"]
                    case "GALXONE":
                        iteraciones["GALXONE"] += 1
                        iteracion = iteraciones["GALXONE"]
                    case "UNKN":
                        iteraciones["UNKN"] += 1
                        iteracion = iteraciones["UNKN"]
                
                date_now = datetime.now() #Toma la fecha actual
                date = date_now.strftime("%d/%m/%Y-%H:%M:%S") #Formatea la fecha a: dd/mm/yy-H:M:S

                status = random.choice(self.estados) #Elige uns estatus random de la lista "estados"

                devise_type = None #Inicializa el tipo de la mision a None

                #Segun la mision se selecciona el tipo de la mision y en caso de ser "UNKN" el tipo de la mision y el estatus se setea a "unknown"
                match mission:
                    case "ORBONE": 
                        devise_type = self.devise_type[0]
                    case "CLNM": 
                        devise_type = self.devise_type[1]
                    case "TMRS": 
                        devise_type = self.devise_type[2]
                    case "GALXONE":
                        devise_type = self.devise_type[3]
                    case "UNKN":
                        devise_type="unknown"
                        status="unknown"
                
                hash_file = None # Se inicializa el hash del objeto a None

                #Si la mision es "UNKN" el hash se setea a "unknown" y en caso contrario se calcula el hash
                if mission != "UNKN":
                    hash_file = hash((
                            'date', date,
                            'mission', mission,
                            'devise_type', devise_type,
                            'devise_status', status
                        ))
                else:
                    hash_file = "unknown"
                

                mission_list = [] #Lista de los elementos de la mision
                mision_dic = {} #Dicionario de los elementos de la mision
                mision_dic['date'] = date
                mision_dic['mission'] = mission
                mision_dic['devise_type'] = devise_type
                mision_dic['devise_status']=status
                mision_dic['hash'] = hash_file

                mission_list.append(mision_dic)

                archivo.generar_archivo(mission_list, iteracion) #Se llama la funcion generar_archivo con el parametro de misiones y el parametro iteracion

                progress_bar(i, num_archivos)

        except Exception as error:
            print("\nAn error occurred:", type(error).__name__, "-", error)

    def generar_informes(self):
        # Lógica para la generación de informes
        pass
        

    def limpiar_archivos_procesados(self):
        # Lógica para la limpieza de archivos
        pass

    def generar_tablero_control(self):
        # Lógica para la generación del tablero de control
        pass