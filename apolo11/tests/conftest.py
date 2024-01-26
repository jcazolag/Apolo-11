import pytest
from apolo11.utilitarios.date import DateUtil as du
from apolo11.utilitarios.archivos import ArchivosUtil as au

@pytest.fixture(scope="session")
def app(request):

    class App:
        pass

    app = App()
    app.obtener_datetime_actual = du.obtener_datetime_actual
    app.obtener_datetime_actual_easy_format = du.obtener_datetime_actual_easy_format
    app.guardar_archivo = au.guardar_archivo

    return app
