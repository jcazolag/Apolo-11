import pytest
from apolo11.utilitarios.date import DateUtil as du

@pytest.fixture(scope="session")
def app(request):

    class App:
        pass

    app = App()
    app.obtener_datetime_actual = du.obtener_datetime_actual
    app.obtener_datetime_actual_easy_format = du.obtener_datetime_actual_easy_format

    return app
