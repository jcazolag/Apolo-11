import pandas as pd
from .project_utils import *

class Generador:
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia

    def generar_archivo(self, mission_list, iteracion):
        try:
            df = pd.DataFrame(mission_list)
            df.to_csv(f"{self.ruta_preferencia}\\APL{mission_list[0]['mission']}-{iteracion}.log", index=None, sep=";", encoding='utf-8-sig')
        except Exception as error:
            ErrorFormat(error)

    def generar_informe(self):
        try:
            data: dict = []
            data = ObtenerData(self.ruta_preferencia)
            print(data)
        except Exception as error:
            ErrorFormat(error)