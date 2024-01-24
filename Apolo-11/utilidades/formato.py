class FormatoUtil:
    
    @staticmethod
    def error_format(error: Exception):
        print("\nAn error occurred:", type(error).__name__, "-", error)
