from utilitarios.formato import FormatoUtil as fu
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.date import DateUtil as du

class GeneradorInformes:
    """Esta clase se encarga de leer los datos de las misiones de cada simulación para generar un reporte organizado.
    """


    def __init__(self, ruta_devices: str, ruta_reportes: str):
        """Parámetros de inicialización de la clase GeneradorInformes.

        :param ruta_devices: Ubicación de la carpeta "devices" donde se almacenaran los informes generados
        :type ruta_devices: str
        """
        self.ruta_devices = ruta_devices
        self.ruta_reportes = ruta_reportes


    def generar(self, nro_simulacion: int):
        """Genera un archivo con el reporte de la información obtenida de los datos arrojados en las simulaciones.

        :param nro_simulacion: Numero de simulación ejecutada.
        :type nro_simulacion: int
        """
        try:
            list_result: dict = {}
            data = au.obtener_data(self.ruta_devices)
            
            # reporte análisis de eventos
            result_1: dict = self.generar_reporte_analisis_eventos(data)
            list_result["Analisis de eventos"] = result_1
            
            # reporte gestión de desconexiones
            result_2: dict = self.generar_reporte_gestion_desconexiones(data)
            list_result["Gestion de desconexiones"] = result_2
            
            # reporte consolidacion de misiones
            result_3: dict = self.generar_reporte_consolidacion_misiones(data)
            list_result["Consolidacion misiones"] = result_3
            
            # reporte calculo de porcentajes
            result_4: dict = self.generar_reporte_calculo_porcentaje(data)
            list_result["Calculo de porcentajes"] = result_4
            
            # guardar reporte de la simulacion
            date: str = du.obtener_datetime_actual()
            path_reportes:str = f"{self.ruta_reportes}\\APLSTATS-REPORTE-{str(date)}.log"
            au.guardar_archivo(list_result, path_reportes)
            print(f"El reporte de la simulacion {nro_simulacion} se guardo en la carpeta de reportes")
        except Exception as error:
            fu.error_format(error)


    def generar_reporte_analisis_eventos(self, data: list) -> dict:
        """Realiza un conteo de eventos por estado para dos criterios: Misión y Dispositivo.

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Reporte de los eventos ocurridos en la simulación según la misión y el dispositivo.
        :rtype: list
        """

        try:
            result: dict = {}
            index: int = 0
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result.values() if d['device_status'] in values 
                    and d["mission"] in values 
                    and d["device_type"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                else:
                    item_dict: dict = {}
                    item_dict["device_status"] = item["device_status"]
                    item_dict["mission"] = item["mission"]
                    item_dict["device_type"] = item["device_type"]
                    item_dict["count"] = 1
                    result[index] = item_dict
                    index += 1
            return result
        except Exception as error:
            fu.error_format(error)



    def generar_reporte_gestion_desconexiones(self, data: list) -> dict:
        """Conteo de desconexiones (Estado: Unknown) agrupado por dispositivos.

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Reporte de las desconexiones identificadas en la simulación agrupadas por misión y los dispositivos en los que se encontraron.
        :rtype: list
        """
        try:
            result: dict = {}
            index: int = 0
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result.values() if d["device_type"] in values 
                    and d["mission"] in values 
                    and d["device_status"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                else:
                    if item["device_status"] == "unknown":
                        item_dict = {}
                        item_dict["device_type"] = item["device_type"]
                        item_dict["mission"] = item["mission"]
                        item_dict["device_status"] = item["device_status"]
                        item_dict["count"] = 1
                        result[index] = item_dict
                        index += 1
            return result
        except Exception as error:
            fu.error_format(error)



    def generar_reporte_consolidacion_misiones(self, data: list) -> dict:
        """Identifica todas las misiones en las que el estado del dispositivo es inoperable y se reporta como "killed"

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Lista de misiones en las que el estado del dispositivo es inoperable
        :rtype: list
        """
        try:
            result: dict = {}
            index: int = 0
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result.values() if d["mission"] in values
                    and d["device_status"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                else:
                    if item["device_status"] == "killed":
                        item_dict = {}
                        item_dict["mission"] = item["mission"]
                        item_dict["device_status"] = item["device_status"]
                        item_dict["count"] = 1
                        result[index] = item_dict
                        index += 1
            return result
        except Exception as error:
            fu.error_format(error)


    def generar_reporte_calculo_porcentaje(self, data: list) -> dict:
        """Contabiliza el porcentaje de datos generados por cada dispositivo y misión contra el total de datos de la simulación.

        :param data: Lista de datos generada a partir de todos los archivos de la simulación.
        :type data: list
        :return: Lista misiones simuladas agrupadas por dispositivo y su porcentaje con respecto a la totalidad de archivos de la simulación.
        :rtype: list
        """
        try:
            result: dict = {}
            index: int = 0
            total: int = len(data)
            for item in data:
                values = item.values()
                value_exists = [
                    d for d in result.values() if d["mission"] in values
                    and d["device_type"] in values
                ]
                if len(value_exists) > 0:
                    value_exists[0]["count"] += 1
                    porcentage = round((value_exists[0]["count"]/total) * 100, 1)
                    value_exists[0]["porcentage"] = porcentage
                else:
                    item_dict = {}
                    item_dict["mission"] = item["mission"]
                    item_dict["device_type"] = item["device_type"]
                    item_dict["count"] = 1
                    item_dict["porcentage"] = round((1/total) * 100, 1)
                    result[index] = item_dict
                    index += 1
            return result
        except Exception as error:
            fu.error_format(error)
