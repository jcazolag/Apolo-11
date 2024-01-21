import pandas as pd
from utilidades.formato import FormatoUtil as fu
from utilidades.archivos import ArchivosUtil as au

class GeneradorInformes:
    def __init__(self, ruta_devices):
        self.ruta_devices = ruta_devices

    def generar(self):
        try:
            date: str = fu.obtener_datetime_actual()
            print(date)
            path_reportes:str = f"{self.ruta_devices}\\APLSTATS-REPORTE-{str(date)}.log"
            df = self.obtener_data()
            self.generar_reporte_analisis_eventos(df, path_reportes)
            # print(df)
        except Exception as error:
            fu.error_format(error)

    def obtener_data(self) -> pd.DataFrame:
        try:
            files = au.files_search(".log", self.ruta_devices)
            if files is not None:
                path: str = f"{self.ruta_devices}\\ALL-DATA.log"
                df = pd.read_json(path)
                return df
        except Exception as error:
            fu.error_format(error)

    def generar_reporte_analisis_eventos(self, df: pd.DataFrame, path: str):
        try:
            df1 = df.groupby(
                [
                    'device_status',
                    'mission',
                    'device_type'
                ])['mission'].count()
            au.guardarDataFrame(df1, path)
            print(df1)
        except Exception as error:
            fu.error_format(error)
