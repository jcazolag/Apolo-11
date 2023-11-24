import os
import random
from datetime import datetime
from .generador import GenerarArchivo

class Apolo11Simulador:
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia
        self.misiones = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]

    def ejecutar_simulacion(self, intervalo=20, max_archivos=random.randint(1, 100)):
        # Lógica para la simulación
        try:
            print(f"Intervalos: {intervalo} segundos")
            print(f"Archivos: {max_archivos}")
            self.generar_archivos(max_archivos)
        except Exception as error:
            print("An error occurred:", type(error).__name__, "-", error)

    def generar_archivos(self, num_archivos):
        # Lógica para la generación de archivos
        try:
            archivo = GenerarArchivo(self.ruta_preferencia) #Se inicializa el objeto de la clase GenerarArchivo

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

            #Bucle para crear la cantidad de archivos dado por la variable "num_archivos"
            for i in range(1,num_archivos+1):
                mision=random.choice(self.misiones)
                match mision:
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
                
                archivo.generar_archivo(mision, iteracion) #Se llama la funcion generar_archivo con el parametro de misiones y el parametro iteracion
        except Exception as error:
            print("An error occurred:", type(error).__name__, "-", error)

    def generar_informes(self):
        # Lógica para la generación de informes
        pass

    def limpiar_archivos_procesados(self):
        # Lógica para la limpieza de archivos
        pass

    def generar_tablero_control(self):
        # Lógica para la generación del tablero de control
        pass