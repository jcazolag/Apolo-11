import os
import random
from datetime import datetime
import pandas as pd

class GenerarArchivo:
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia

    def generar_archivo(self, mission_list, iteracion, code_mission):
        try:
            # Lógica para la generación de archivos
            #Se crea el DataFrame del objeto con los datos 
            df = pd.DataFrame(mission_list)
            #Se crea el archivo csv a partir del DataFrame con la ruta definida
            df.to_csv(f"{self.ruta_preferencia}\\APL{code_mission}-{iteracion}.log", index=False, sep=";", encoding='utf-8-sig')
        except Exception as error:
            #print(f"Error: {error}")
            print("\nAn error occurred:", type(error).__name__, "-", error)

    def generar_informe(self):
        try:
            # Lógica para la generación de informes
            #Se crea el DataFrame del objeto con los datos 
            df = pd.DataFrame()

            #Se crea el archivo csv a partir del DataFrame con la ruta definida
            #df.to_csv(f"{self.ruta_preferencia}\\.log", index=False, sep=";", encoding='utf-8-sig')
            
        except Exception as error:
            #print(f"Error: {error}")
            print("\nAn error occurred:", type(error).__name__, "-", error)
        
        pass