class FormatoUtil:
    """Esta clase contiene el método que determina el formato en que se mostraran los errores en caso de presentarse.
    """
    
    @staticmethod
    def error_format(error: Exception):
        """Método para mostrar los errores en caso de presentarse.

        :param error: Error encontrado.
        :type error: Exception
        """
        print("\nAn error occurred:", type(error).__name__, "-", error)
