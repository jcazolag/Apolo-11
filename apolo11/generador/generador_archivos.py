import pandas as pd
import random
from utilitarios.formato import FormatoUtil as fu
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.date import DateUtil as du


class GeneradorArchivos:
    
    def __init__(self, ruta_devices):
        self.ruta_devices = ruta_devices
        self.config = au.load_config()
        self.misiones = self.config['tipos_misiones']
        self.estados = self.config['estados_misiones']
        self.device_type = self.config['tipos_devices']
        self.mision_name = self.config['nombres_misiones']

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

            print(f"Se generaron {num_archivos} archivo(s)", end="\n")

            list_dates: list = []
            list_missions: list = []
            list_devices_types: list = []
            list_devices_status: list = []
            list_hashes: list = []

            for i in range(num_archivos):
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
                
                date = du.obtener_datetime_actual()
                status = random.choice(self.estados)
                device_type = None

                match mission:
                    case "ORBONE": 
                        device_type = self.device_type[0]
                        mision_name = self.mision_name[0]
                    case "CLNM": 
                        device_type = self.device_type[1]
                        mision_name = self.mision_name[1]
                    case "TMRS": 
                        device_type = self.device_type[2]
                        mision_name = self.mision_name[2]
                    case "GALXONE":
                        device_type = self.device_type[3]
                        mision_name = self.mision_name[3]
                    case "UNKN":
                        mision_name = random.choice(self.mision_name)
                        device_type = random.choice(self.device_type)
                        status="unknown"
                
                hash_file = None

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

                mision_dic = {}
                mision_dic["date"] = date
                mision_dic["mission"] = mision_name
                mision_dic["device_type"] = device_type
                mision_dic["device_status"]= status
                mision_dic["hash"] = hash_file

                file_path: str = f"{self.ruta_devices}\\APL{mission}-{iteracion}.log"
                
                au.guardar_archivo(mision_dic, file_path)

                list_dates.append(date)
                list_missions.append(mision_name)
                list_devices_types.append(device_type)
                list_devices_status.append(status)
                list_hashes.append(hash_file)
        except Exception as error:
            fu.error_format(error)
