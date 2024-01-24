from utilidades.formato import FormatoUtil as fu
from utilidades.archivos import ArchivosUtil as au
from utilidades.date import DateUtil as du

class GeneradorInformes:


    def __init__(self, ruta_devices: str):
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
            
            # reporte calculo de porcentajes
            result_4: dict = self.generar_reporte_calculo_porcentaje(data)
            dict_4 = {"Calculo de porcentajes": result_4}
            list_result.append(dict_4)
            
            date: str = du.obtener_datetime_actual()
            path_reportes:str = f"{self.ruta_devices}\\APLSTATS-REPORTE-{str(date)}.log"
            au.guardar_archivo(list_result, path_reportes)
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


    def generar_reporte_calculo_porcentaje(self, data: list):
        try:
            result: list = []
            total: int = len(data)
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result if d["mission"] in values
                    and d["device_type"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                    porcentage = round((value_exists[0]["count"]/total) * 100, 1)
                    value_exists[0]["porcentage"] = f"{porcentage}%"
                else:
                    dict = {}
                    dict["mission"] = item["mission"]
                    dict["device_type"] = item["device_type"]
                    dict["count"] = 1
                    dict["porcentage"] = f"{round((1/total) * 100, 1)}%"
                    result.append(dict)
            return result
        except Exception as error:
            fu.error_format(error)


    def generar_tablero_control(self, simulacion: int, data: list):
        try:
            config = au.load_config()
            # total: int = len(data)
            # nro_simulacion: int = simulacion
            # actual_datetime: str = du.obtener_datetime_actual()
            # mission_names: list = config["nombres_misiones"]
            # devices_type: list = config["tipos_devices"]
            # devices_status: list = config["estados_misiones"]
            # result: dict = {
            #     "Resumen simulacion": {
            #         "Simulacion": 
            #         "Cantidad total de archivos": total,
            #     }
            # }
        except Exception as error:
            fu.error_format(error)