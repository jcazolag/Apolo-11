from datetime import datetime
from utilitarios.archivos import ArchivosUtil as au

class DateUtil:
    """Esta clase contiene los métodos para leer la hora actual al momento de ejecutar la simulación.
    """
    
    @staticmethod
    def obtener_datetime_actual() -> str:
        """Obtiene la hora actual con el formato indicado en el archivo config.json

        :return: Hora actual en el formato indicado en el archivo config.json"
        :rtype: str
        """
        config = au.load_config()
        formato_fecha: str = config["formato_fecha"]
        return str(datetime.now().strftime(formato_fecha))


    @staticmethod
    def obtener_datetime_actual_easy_format() -> str:
        """Obtiene la hora actual en formato dd/mm/YYYY-HH:MM:SS

        :return: Hora actual en formato dd/mm/YYYY-HH:MM:SS
        :rtype: str
        """
        config = au.load_config()
        return str(datetime.now().strftime("%d/%m/%Y-%H:%M:%S"))