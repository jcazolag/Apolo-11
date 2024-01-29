from datetime import datetime


def test_obtener_datetime_actual(setup):
    formato_fecha = "%d%m%Y%H%M%S"
    resultado = setup.obtener_datetime_actual
    resultado_esperado = str(datetime.now().strftime(formato_fecha))
    assert resultado_esperado == resultado


def test_obtener_datetime_actual_easy_format(setup):
    resultado = setup.obtener_datetime_actual_easy_format
    resultado_esperado = str(datetime.now().strftime("%d/%m/%Y-%H:%M:%S"))
    assert resultado_esperado == resultado
