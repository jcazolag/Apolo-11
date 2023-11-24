import os
import random
from datetime import datetime
import pandas as pd

class GenerarArchivo:
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia
        self.ruta_devices = os.path.join(ruta_preferencia, "devices")
        self.estados = ["excellent", "good", "warning", "faulty", "killed", "unknown"]
        self.devise_type = ["Satellite fleetl", "Lunar colonization", "Mars Tourism", "Intergalactic exploration"]

    def generar_archivo(self, mission, iteracion):
        try:
            # Lógica para la generación de archivos

            date_now = datetime.now() #Toma la fecha actual
            date = date_now.strftime("%d%m%Y%H%M%S") #Formatea la fecha a: ddmmyyHHMISS

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

            #Se crea el DataFrame del objeto con los datos 
            df = pd.DataFrame({

                'date': [date],
                'mission': [mission],
                'devise_type': [devise_type],
                'devise_status': [status],
                'hash': [hash_file]
            })

            #Se crea el archivo .csv a partir del DataFrame con la ruta definida
            df.to_csv(f"{self.ruta_devices}\\APL{mission}-{iteracion}.csv", index=False)
            
        except Exception as error:
            #print(f"Error: {error}")
            print("An error occurred:", type(error).__name__, "-", error)
