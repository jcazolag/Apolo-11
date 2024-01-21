from datetime import datetime

class FormatoUtil:
    
    @staticmethod
    def obtener_datetime_actual() -> str:
        return str(datetime.now().strftime("%d%m%Y%H%M%S"))
    
    @staticmethod
    def error_format(error: Exception):
        print("\nAn error occurred:", type(error).__name__, "-", error)
