import os


class PresentacionUtil:
    """Clase que contiene métodos para mejorar la presentación del programa.
    """

    @staticmethod
    def progress_bar(progress: int, total: int):
        """Barra de progreso en la generación de archivos.

        :param progress: Archivos generados para calcular el porcentaje de progreso.
        :type progress: int
        :param total: Total de archivos a generar.
        :type total: int
        """
        percent = 100 * (progress/float(total))
        bar = '█' * int(percent) + '-' * (100-int(percent))
        print(f"\r|{bar}| {percent:.2f}%", end="\r")
        if progress == total:
            print(f"\r|{bar}| {percent:.2f}%", end="\r\n\n")


    @staticmethod
    def limpiar_consola():
        """Método para limpiar la consola. 
        """
        os.system("cls")
