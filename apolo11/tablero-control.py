import os
import pandas as pd
from utilitarios.formato import FormatoUtil as fu
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.date import DateUtil as du


def GenerarTableroControl():
    """Clase para generar el archivo e imprimir el tablero de control
    """
    try:
        ruta_preferencia = os.path.join(os.getcwd(), "files")
        ruta_reportes = os.path.join(ruta_preferencia, "reportes")
        au.validar_path(ruta_preferencia)
        au.validar_path(ruta_reportes)
        data: list = au.obtener_data(ruta_reportes)
        result_tablero: dict = {}
        analisis_eventos: dict = {}
        gestion_desconexiones: dict = {}
        consolidacion_misiones: dict = {}
        calculo_porcentajes: dict = {}
        index_analisis: int = 0
        index_gestion_desconexiones: int = 0
        index_consolidacion_misiones: int = 0
        index_calculo_porcentajes: int = 0
        for simulacion in data:
            for nombre, values in simulacion.items():
                for item_key, item_value in values.items():
                    match nombre:
                        case "Analisis de eventos":
                            value_exists: bool = False
                            for k,d in analisis_eventos.items():
                                if (
                                    d["device_status"] == item_value["device_status"]
                                    and d["mission"] == item_value["mission"]
                                    and d["device_type"] == item_value["device_type"]
                                ):
                                    value_exists = True
                                    analisis_eventos[k]["count"] += item_value["count"]
                            if (value_exists is False):
                                item_dict: dict = {}
                                item_dict["device_status"] = item_value["device_status"]
                                item_dict["mission"] = item_value["mission"]
                                item_dict["device_type"] = item_value["device_type"]
                                item_dict["count"] = item_value["count"]
                                analisis_eventos[index_analisis] = item_dict
                                index_analisis += 1
                        case "Gestion de desconexiones":
                            value_exists: bool = False
                            for k,d in gestion_desconexiones.items():
                                if (
                                    d["device_type"] == item_value["device_type"]
                                    and d["mission"] == item_value["mission"]
                                    and d["device_status"] == item_value["device_status"]
                                ):
                                    value_exists = True
                                    gestion_desconexiones[k]["count"] += item_value["count"]
                            if (value_exists is False):
                                item_dict: dict = {}
                                item_dict["device_type"] = item_value["device_type"]
                                item_dict["mission"] = item_value["mission"]
                                item_dict["device_status"] = item_value["device_status"]
                                item_dict["count"] = item_value["count"]
                                gestion_desconexiones[index_gestion_desconexiones] = item_dict
                                index_gestion_desconexiones += 1
                        case "Consolidacion misiones":
                            value_exists: bool = False
                            for k,d in consolidacion_misiones.items():
                                if (
                                    d["mission"] == item_value["mission"]
                                    and d["device_status"] == item_value["device_status"]
                                ):
                                    value_exists = True
                                    consolidacion_misiones[k]["count"] += item_value["count"]
                            if (value_exists is False):
                                item_dict: dict = {}
                                item_dict["mission"] = item_value["mission"]
                                item_dict["device_status"] = item_value["device_status"]
                                item_dict["count"] = item_value["count"]
                                consolidacion_misiones[index_consolidacion_misiones] = item_dict
                                index_consolidacion_misiones += 1
                        case "Calculo de porcentajes":
                            value_exists: bool = False
                            for k,d in calculo_porcentajes.items():
                                if (
                                    d["mission"] == item_value["mission"]
                                    and d["device_type"] == item_value["device_type"]
                                ):
                                    value_exists = True
                                    calculo_porcentajes[k]["count"] += item_value["count"]
                                    calculo_porcentajes[k]["porcentage"] += item_value["porcentage"]
                            if (value_exists is False):
                                item_dict: dict = {}
                                item_dict["mission"] = item_value["mission"]
                                item_dict["device_type"] = item_value["device_type"]
                                item_dict["count"] = item_value["count"]
                                item_dict["porcentage"] = item_value["porcentage"]
                                calculo_porcentajes[index_calculo_porcentajes] = item_dict
                                index_calculo_porcentajes += 1
        result_tablero["Analisis de eventos"] = analisis_eventos
        result_tablero["Gestion de desconexiones"] = gestion_desconexiones
        result_tablero["Consolidacion misiones"] = consolidacion_misiones
        result_tablero["Calculo de porcentajes"] = calculo_porcentajes
        fecha: str = du.obtener_datetime_actual()
        path: str = f"{ruta_preferencia}\\TABLERO-CONTROL-{fecha}.log"
        au.guardar_archivo(result_tablero, path)
        result_data = au.load_file(path)
        for nombre_reporte, values_reporte in result_data.items():
            print("\n" + nombre_reporte, end="\n")
            df = pd.DataFrame.from_dict(values_reporte.values())
            print(df)
    except Exception as error:
        fu.error_format(error)


if __name__ == "__main__":
    try:
        GenerarTableroControl()
    except Exception as error:
        fu.error_format(error)