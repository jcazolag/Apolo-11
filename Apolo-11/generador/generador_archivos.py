import pandas as pd
import random
from time import sleep
from datetime import datetime
import utilidades.util as util

class GeneradorArchivos:
    
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia
        self.misiones = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
        self.estados = ["excellent", "good", "warning", "faulty", "killed", "unknown"]
        self.device_type = ["Satelite", "Ship", "Space suite", "Space vehicle"]

    def generar(self, num_archivos):
        try:            
            # Iteración de los archivos creado por cada mision
            iteraciones = {
                "ORBONE": 0,
                "CLNM": 0,
                "TMRS": 0,
                "GALXONE": 0,
                "UNKN": 0
            }
            iteracion: int = 0 

            print(f"Generando {num_archivos} archivo(s):", end="\n")
            util.progress_bar(0, num_archivos)

            for i in range(1, num_archivos + 1):
                sleep(0.1)
                mission: str = random.choice(self.misiones)
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
                
                date_now = datetime.now()
                date = date_now.strftime("%d/%m/%Y-%H:%M:%S") # Formatea la fecha a: dd/mm/yy-H:M:S
                status = random.choice(self.estados) # Elige uns estatus random de la lista "estados"
                device_type = None #I nicializa el tipo de la mision a None

                # Segun la mision se selecciona el tipo de la mision y en caso de ser "UNKN" el tipo de la mision y el estatus se setea a "unknown"
                match mission:
                    case "ORBONE": 
                        device_type = self.device_type[0]
                    case "CLNM": 
                        device_type = self.device_type[1]
                    case "TMRS": 
                        device_type = self.device_type[2]
                    case "GALXONE":
                        device_type = self.device_type[3]
                    case "UNKN":
                        device_type="unknown"
                        status="unknown"
                
                hash_file = None # Se inicializa el hash del objeto a None

                # Si la mision es "UNKN" el hash se setea a "unknown" y en caso contrario se calcula el hash
                if mission != "UNKN":
                    hash_file = hash((
                            'date', date,
                            'mission', mission,
                            'device_type', device_type,
                            'device_status', status
                        ))
                else:
                    hash_file = "unknown"
                
                mission_list = [] #Lista de los elementos de la mision
                mision_dic = {} #Dicionario de los elementos de la mision
                mision_dic['date'] = date
                mision_dic['mission'] = mission
                mision_dic['device_type'] = device_type
                mision_dic['device_status']= status
                mision_dic['hash'] = hash_file
                mission_list.append(mision_dic)
                self.guardar(mission_list, iteracion) #Se llama la funcion generar_archivo con el parametro de misiones y el parametro iteracion
                
                util.progress_bar(i, num_archivos)
        except Exception as error:
            util.error_format(error)

    def guardar(self, mission_list, iteracion):
        try:
            df = pd.DataFrame(mission_list)
            df.to_csv(f"{self.ruta_preferencia}\\APL{mission_list[0]['mission']}-{iteracion}.log", index=None, sep=";", encoding='utf-8-sig')
        except Exception as error:
            util.error_format(error)