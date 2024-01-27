import os
import pandas as pd
from utilitarios.formato import FormatoUtil as fu
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.date import DateUtil as du


def GenerarTableroControl():
    try:
        ruta_preferencia = os.path.join(os.getcwd(), "files")
        ruta_reportes = os.path.join(ruta_preferencia, "reportes")
        data: list = au.obtener_data(ruta_reportes)
        print(data)
        df = pd.DataFrame(data)
        # print(df)
        # fecha_actual: str = du.obtener_datetime_actual()
        # df.to_csv(f"{ruta_reportes}\\RESUMEN-TABLERO-CONTROL-{fecha_actual}.csv", index=False)
        # # print(df)
    except Exception as error:
        fu.error_format(error)


if __name__ == "__main__":
    try:
        GenerarTableroControl()
    except Exception as error:
        fu.error_format(error)