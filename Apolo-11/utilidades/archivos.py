import os
import pandas as pd
from time import sleep
from utilidades.formato import FormatoUtil as fu
from utilidades.presentacion import PresentacionUtil as pu

class ArchivosUtil:
    
    @staticmethod
    def files_search(extension, path):
        try:
            archivos = os.listdir(path)
            archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]
            if archivos_con_extension:
                return archivos_con_extension
            else:
                return None
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def file_remove(extension, path):
        try:
            archivos = os.listdir(path)
            archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]
            if archivos_con_extension is not None:
                print("\nEliminando archivos:", end="\n")
                pu.progress_bar(0, len(archivos_con_extension))
                i = 0
                for archivo in archivos_con_extension:
                    sleep(0.1)
                    ruta_archivo = os.path.join(path, archivo)
                    os.remove(ruta_archivo)
                    i+=1
                    pu.progress_bar(i,len(archivos_con_extension))

                print(f"\nSe eliminaron {len(archivos_con_extension)} archivos")
            else:
                print("No se encontraron archivos")
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def validar_path(path: str):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
        except Exception as error:
            fu.error_format(error)

