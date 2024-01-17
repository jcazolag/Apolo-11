from utilidades.formato import FormatoUtil as fu

class GeneradorInformes():
    def __init__(self, ruta_preferencia):
        self.ruta_preferencia = ruta_preferencia

    def generar(self):
        try:
            data: dict = []
            #data = util.obtener_data(self.ruta_preferencia)
            print(data)
        except Exception as error:
            fu.error_format(error)
