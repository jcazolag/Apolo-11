from datetime import datetime
from utilidades.archivos import ArchivosUtil as au

class DateUtil:
    
    @staticmethod
    def obtener_datetime_actual() -> str:
        config = au.load_config()
        formato_fecha: str = config["formato_fecha"]
        return str(datetime.now().strftime(formato_fecha))