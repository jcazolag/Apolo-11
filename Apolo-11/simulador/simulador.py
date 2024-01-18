import os
import random
import generador.generador_archivos as ga
import generador.generador_informes as gi
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

    def ejecutar_simulacion(self, intervalo: int = 20, num_archivos: int = random.randint(1, 100)):
        try:
            generador_archivos = ga.GeneradorArchivos(self.ruta_devices)
            generador_informes = gi.GeneradorInformes(self.ruta_devices)
            generador_archivos.generar(num_archivos)
            generador_informes.generar()
        except Exception as error:
            fu.error_format(error)
