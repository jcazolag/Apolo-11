import os
import pandas as pd
from utilitarios.formato import FormatoUtil as fu
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.date import DateUtil as du


def GenerarTableroControl():
    try:
        ruta_preferencia = os.path.join(os.getcwd(), "files")
        ruta_reportes = os.path.join(ruta_preferencia, "reportes")
        au.validar_path(ruta_preferencia)
        au.validar_path(ruta_reportes)
        data: list = au.obtener_data(ruta_reportes)
        
        analisis_eventos: dict = {}
        gestion_desconexiones: dict = {}
        consolidacion_misiones: dict = {}
        calculo_porcentajes: dict = {}
        for simulacion in data:
            for nombre, values in simulacion.items():
                for item_key, item_value in values.items():
                    # print("nombre: ", item_key)
                    # print("value: ", item_value)
                    # for d in analisis_eventos.values():
                    #     if (d["device_status"] in item_value.values()
                    #         and d["mission"] in item_value.values() and d["device_type"] in item_value.values()):
                            
                    # print(analisis_eventos)
                    if (nombre == "Analisis de eventos"):
                        value_exists = [
                            d for d in analisis_eventos.values() if d["device_status"] in item_value.values() 
                            and d["mission"] in item_value.values()
                            and d["device_type"] in item_value.values()
                        ]
                        # print(value_exists)
                        if len(value_exists) > 0:
                            # print(analisis_eventos)
                            print(value_exists)
                            value_exists[0]["count"] += item_value["count"]
                        else:
                            item_dict: dict = {}
                            item_dict["device_status"] = item_value["device_status"]
                            item_dict["mission"] = item_value["mission"]
                            item_dict["device_type"] = item_value["device_type"]
                            item_dict["count"] = 1
                            # print(item_dict)
                            analisis_eventos[item_key] = item_dict
        # print(analisis_eventos)
    except Exception as error:
        fu.error_format(error)


if __name__ == "__main__":
    try:
        GenerarTableroControl()
    except Exception as error:
        fu.error_format(error)