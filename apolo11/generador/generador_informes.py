from utilitarios.formato import FormatoUtil as fu
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.date import DateUtil as du

class GeneradorInformes:
    """Esta clase se encarga de leer los datos de las misiones de cada simulación para generar un reporte organizado.
    """

    def __init__(self, ruta_devices: str):
        """Parámetros de inicialización de la clase GeneradorInformes.

        :param ruta_devices: Ubicación de la carpeta "devices" donde se almacenaran los informes generados
        :type ruta_devices: str
        """
        self.ruta_devices = ruta_devices


    def generar(self, nro_simulacion: int):
        """Genera un archivo con el reporte de la información obtenida de los datos arrojados en las simulaciones.

        :param nro_simulacion: Numero de simulación ejecutada.
        :type nro_simulacion: int
        """
        try:
            list_result: list = []
            data: list = au.obtener_data(self.ruta_devices)
            
            # reporte análisis de eventos
            result_1: dict = self.generar_reporte_analisis_eventos(data)
            dict_1: dict = {"Analisis de eventos": result_1}
            list_result.append(dict_1)
            
            # reporte gestión de desconexiones
            result_2: dict = self.generar_reporte_gestion_desconexiones(data)
            dict_2: dict = {"Gestion de desconexiones": result_2}
            list_result.append(dict_2)
            
            # reporte consolidacion de misiones
            result_3: dict = self.generar_reporte_consolidacion_misiones(data)
            dict_3: dict = {"Consolidacion misiones": result_3}
            list_result.append(dict_3)
            
            # reporte calculo de porcentajes
            result_4: dict = self.generar_reporte_calculo_porcentaje(data)
            dict_4: dict = {"Calculo de porcentajes": result_4}
            list_result.append(dict_4)
            
            date: str = du.obtener_datetime_actual()
            path_reportes: str = f"{self.ruta_devices}\\APLSTATS-REPORTE-{str(date)}.log"
            au.guardar_archivo(list_result, path_reportes)

            result_tablero_control: dict = self.generar_tablero_control(data, nro_simulacion)
            path_tablero_control: str = f"{self.ruta_devices}\\APLSTATS-TABLERO-CONTROL-{str(date)}.log"
            au.guardar_archivo(result_tablero_control, path_tablero_control)
        except Exception as error:
            fu.error_format(error)


    def generar_reporte_analisis_eventos(self, data: list) -> list:
        """Realiza un conteo de eventos por estado para dos criterios: Misión y Dispositivo.

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Reporte de los eventos ocurridos en la simulación según la misión y el dispositivo.
        :rtype: list
        """
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
        """Conteo de desconexiones (Estado: Unknown) agrupado por dispositivos.

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Reporte de las desconexiones identificadas en la simulación agrupadas por misión y los dispositivos en los que se encontraron.
        :rtype: list
        """
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
        """Identifica todas las misiones en las que el estado del dispositivo es inoperable y se reporta como "killed"

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Lista de misiones en las que el estado del dispositivo es inoperable
        :rtype: list
        """
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


    def generar_reporte_calculo_porcentaje(self, data: list) -> list:
        """Contabiliza el porcentaje de datos generados por cada dispositivo y misión contra el total de datos de la simulación.

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Lista misiones simuladas agrupadas por dispositivo y su porcentaje con respecto a la totalidad de archivos de la simulación.
        :rtype: list
        """
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


    def generar_tablero_control(self, data: list, nro_simulacion: int) -> dict:
        """Reporte general de las simulaciones ejecutadas.

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :param nro_simulacion: Numero de simulación ejecutada.
        :type nro_simulacion: int
        :return: Diccionario de reporte con los datos relevantes de las simulaciones llevadas a cabo.
        :rtype: dict
        """
        try:
            config = au.load_config()
            total: int = len(data)
            actual_datetime: str = du.obtener_datetime_actual_easy_format()
            mission_names: list = config["nombres_misiones"]
            devices_type: list = config["tipos_devices"]
            devices_status: list = config["estados_misiones"]
            result: dict = {
                "Resumen simulacion": {
                    "Simulacion": nro_simulacion,
                    "Cantidad total de archivos": total,
                    "Fecha de ejecución": actual_datetime,
                    "Misiones": ', '.join(map(str, mission_names)),
                    "Tipos de dispositivos": ', '.join(map(str, devices_type)),
                    "Estados": ', '.join(map(str, devices_status))
                }
            }
            return result
        except Exception as error:
            fu.error_format(error)