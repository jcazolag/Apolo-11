import pandas as pd
from utilidades.formato import FormatoUtil as fu
from utilidades.archivos import ArchivosUtil as au

class GeneradorInformes():
    def __init__(self, ruta_devices):
        self.ruta_devices = ruta_devices

    def generar(self):
        try:
            df = self.obtener_data()  
            print(df)
        except Exception as error:
            fu.error_format(error)

    def obtener_data(self) -> pd.DataFrame:
        try:
            files = au.files_search(".log", self.ruta_devices)
            if files is not None:
                list_df: list = []
                index: int = 0
                for file in files:
                    path = f"{self.ruta_devices}/{file}"
                    df = pd.read_csv(path, sep=";")
                    list_df.append(df)
                result: pd.DataFrame = pd.concat(list_df)
                return result
        except Exception as error:
            fu.error_format(error)
