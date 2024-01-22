import pandas as pd
from utilidades.formato import FormatoUtil as fu
from utilidades.archivos import ArchivosUtil as au

class GeneradorInformes:


    def __init__(self, ruta_devices):
        self.ruta_devices = ruta_devices


    def generar(self):
        try:
            list_result: list = []
            data = au.obtener_data(self.ruta_devices)
            
            # reporte análisis de eventos
            result_1: dict = self.generar_reporte_analisis_eventos(data)
            dict_1 = {"Analisis de eventos": result_1}
            list_result.append(dict_1)
            
            # reporte gestión de desconexiones
            result_2: dict = self.generar_reporte_gestion_desconexiones(data)
            dict_2 = {"Gestion de desconexiones": result_2}
            list_result.append(dict_2)
            
            # reporte consolidacion de misiones
            result_3: dict = self.generar_reporte_consolidacion_misiones(data)
            dict_3 = {"Consolidacion misiones": result_3}
            list_result.append(dict_3)
            
            date: str = fu.obtener_datetime_actual()
            path_reportes:str = f"{self.ruta_devices}\\APLSTATS-REPORTE-{str(date)}.log"
            au.save_file(list_result, path_reportes)
        except Exception as error:
            fu.error_format(error)


    def generar_reporte_analisis_eventos(self, data: list) -> list:
        try:
            result: list = []
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result if d['device_status'] in values 
                    and d["mission"] in values 
                    and d["device_type"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                else:
                    dict = {}
                    dict["device_status"] = item["device_status"]
                    dict["mission"] = item["mission"]
                    dict["device_type"] = item["device_type"]
                    dict["count"] = 1
                    result.append(dict)
            return result
        except Exception as error:
            fu.error_format(error)


    def generar_reporte_gestion_desconexiones(self, data: list) -> list:
        try:
            result: list = []
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result if d["device_type"] in values 
                    and d["mission"] in values 
                    and d["device_status"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                else:
                    if item["device_status"] == "unknown":
                        dict = {}
                        dict["device_type"] = item["device_type"]
                        dict["mission"] = item["mission"]
                        dict["device_status"] = item["device_status"]
                        dict["count"] = 1
                        result.append(dict)
            return result
        except Exception as error:
            fu.error_format(error)


    def generar_reporte_consolidacion_misiones(self, data: list) -> list:
        try:
            result: list = []
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result if d["mission"] in values
                    and d["device_status"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                else:
                    if item["device_status"] == "killed":
                        dict = {}
                        dict["mission"] = item["mission"]
                        dict["device_status"] = item["device_status"]
                        dict["count"] = 1
                        result.append(dict)
            return result
        except Exception as error:
            fu.error_format(error)