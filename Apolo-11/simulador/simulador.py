import os
import random
import generador.generador_archivos as ga
import generador.generador_informes as gi
from time import sleep
from utilidades.archivos import ArchivosUtil as au
from utilidades.formato import FormatoUtil as fu
from utilidades.presentacion import PresentacionUtil as pu
from utilidades.archivos import ArchivosUtil as au


class Apolo11Simulador:

    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia
        self.ruta_devices = os.path.join(self.ruta_preferencia, "devices")
        self.ruta_backups = os.path.join(self.ruta_preferencia, "backups")
        au.validar_path(self.ruta_devices)
        au.validar_path(self.ruta_backups)
        self.config = au.load_config()
        self.intervalo_simulacion_default = self.config['intervalo_simulacion']
        self.cantidad_archivos_min_default = self.config['cantidad_archivos_min']
        self.cantidad_archivos_max_default = self.config['cantidad_archivos_max']

    def ejecutar_simulacion(self,
                            intervalo: int = None,
                            num_archivos: int = None):
        try:
            generador_archivos = ga.GeneradorArchivos(self.ruta_devices)
            generador_informes = gi.GeneradorInformes(self.ruta_devices)
            iterator: int = 1
            while (True):
                print(f"Simulacion: {iterator}")
                if (intervalo is None):
                    intervalo: int = self.intervalo_simulacion_default
                if (num_archivos is None):
                    num_archivos: int = random.randint(
                        self.cantidad_archivos_min_default,
                        self.cantidad_archivos_max_default)
                generador_archivos.generar(num_archivos)
                generador_informes.generar()
                iterator += 1
                sleep(intervalo)
        except Exception as error:
            fu.error_format(error)