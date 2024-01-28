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
        list_data = au.obtener_data(ruta_reportes)
        print(list_data)
    except Exception as error:
        fu.error_format(error)


if __name__ == "__main__":
    try:
        GenerarTableroControl()
    except Exception as error:
        fu.error_format(error)