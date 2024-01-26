from datetime import datetime
from apolo11.utilitarios.archivos import ArchivosUtil as au
from apolo11.utilitarios.date import DateUtil as du


def test_obtener_datetime_actual(app):
    config = au.load_config()
    formato_fecha = config["formato_fecha"]
    resultado = du.obtener_datetime_actual()
    resultado_esperado = str(datetime.now().strftime(formato_fecha))
    assert resultado_esperado == resultado


def test_obtener_datetime_actual_easy_format(app):
    config = au.load_config()
    resultado = du.obtener_datetime_actual_easy_format()
    resultado_esperado = str(datetime.now().strftime("%d/%m/%Y-%H:%M:%S"))
    assert resultado_esperado == resultado
