from apolo11.utilitarios.date import DateUtil as du

import pytest

@pytest.fixture(scope="session")
def setup(request):
    class App:
        pass
    app = App()
    app.obtener_datetime_actual = du.obtener_datetime_actual
    app.obtener_datetime_actual_easy_format = du.obtener_datetime_actual_easy_format
    return app
