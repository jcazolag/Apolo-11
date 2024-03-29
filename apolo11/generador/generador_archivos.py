import pandas as pd
import random
from utilitarios.formato import FormatoUtil as fu
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.date import DateUtil as du


class GeneradorArchivos:
    """Esta clase contiene la informacion y procesos necesarios para generar los archivos de las misiones en cada simulación.
    """
    
    def __init__(self, ruta_devices: str) -> None:
        """Parámetros de inicialización de la clase GeneradorArchivos

        :param ruta_devices: Ubicación de la carpeta "devices" donde se almacenaran los archivos generados
        :type ruta_devices: str
        """
        self.ruta_devices = ruta_devices
        self.config = au.load_config()
        self.misiones = self.config['tipos_misiones']
        self.estados = self.config['estados_misiones']
        self.device_type = self.config['tipos_devices']
        self.mision_name = self.config['nombres_misiones']

    def generar(self, num_archivos: int):
        """Genera una cantidad exacta de archivos de las misiones, cantidad definida pro el parámetro "num_archivos".
        Este parámetro puede ser un número aleatorio o una cantidad indicada por el usuario.

        :param num_archivos: Cantidad de archivos a generar
        :type num_archivos: int
        """
        try:            
            # Iteración de los archivos creado por cada mision
            iteraciones: dict = {
                "ORBONE": 0,
                "CLNM": 0,
                "TMRS": 0,
                "GALXONE": 0,
                "UNKN": 0
            }
            iteracion: int = 0 

            print(f"Se generaron {num_archivos} archivo(s)", end="\n")

            for i in range(num_archivos):
                mission: str = random.choice(self.misiones)
                match mission:
                    case "ORBONE": 
                        iteraciones["ORBONE"] += 1
                        iteracion = iteraciones["ORBONE"]
                        mision_name = self.mision_name[0]
                    case "CLNM": 
                        iteraciones["CLNM"] += 1
                        iteracion = iteraciones["CLNM"]
                        mision_name = self.mision_name[1]
                    case "TMRS": 
                        iteraciones["TMRS"] += 1
                        iteracion = iteraciones["TMRS"]
                        mision_name = self.mision_name[2]
                    case "GALXONE":
                        iteraciones["GALXONE"] += 1
                        iteracion = iteraciones["GALXONE"]
                        mision_name = self.mision_name[3]
                    case "UNKN":
                        iteraciones["UNKN"] += 1
                        iteracion = iteraciones["UNKN"]
                        mision_name = random.choice(self.mision_name)
                
                date: str = du.obtener_datetime_actual()
                status: str = random.choice(self.estados)
                device_type: str = random.choice(self.device_type)
                
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

                mision_dic: dict = {}
                mision_dic["date"] = date
                mision_dic["mission"] = mision_name
                mision_dic["device_type"] = device_type
                mision_dic["device_status"]= status
                mision_dic["hash"] = hash_file

                file_path: str = f"{self.ruta_devices}\\APL{mission}-{iteracion}.log"
                
                au.guardar_archivo(mision_dic, file_path)
        except Exception as error:
            fu.error_format(error)
