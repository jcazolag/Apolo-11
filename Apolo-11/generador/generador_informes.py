import utilidades.util as util

class GeneradorInformes():
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia

    def generar(self):
        try:
            data: dict = []
            data = util.obtener_data(self.ruta_preferencia)
            print(data)
        except Exception as error:
            util.error_format(error)