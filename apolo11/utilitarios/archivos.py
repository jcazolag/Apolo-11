import os
import json
from time import sleep
from utilitarios.formato import FormatoUtil as fu
from utilitarios.presentacion import PresentacionUtil as pu


class ArchivosUtil:
    """Esta clase contiene los métodos que interactuan con los archivos generados en la simulación
    """
    @staticmethod
    def guardar_archivo(data: dict, path: str):
        """Método para guardar los archivos generados en la simulación.

        :param data: Datos generados en cada misión de la simulación.
        :type data: list
        :param path: Ruta donde se guardarán los archivos.
        :type path: str
        """
        try:
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def obtener_data(path: str) -> list:
        """Método para leer la información que contienen los datos guardados.

        :param ruta_devices: Ruta donde se almacenan los archivos de la simulación.
        :type ruta_devices: str
        :return: Lista que agrupa los datos de todos los archivos generados en la simulación.
        :rtype: list
        """
        try:
            files = ArchivosUtil.files_search(".log", path)
            result: list = []
            if files is not None:
                for file in files:
                    with open(f"{path}\\{file}") as f:
                        result_file = json.load(f)
                        result.append(result_file)
                return result
            else:
                return None
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def files_search(extension: str, path: str) -> list:
        """Método para buscar archivos guardados de la simulación.

        :param extension: La extensión o tipo de archivo a buscar.
        :type extension: str
        :param path: Ruta o ubicación donde se buscarán los archivos.
        :type path: str
        :return: Archivos encontrados en la ubicación indicada.
        :rtype: list
        """
        try:
            archivos = os.listdir(path)
            archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]
            if archivos_con_extension:
                return archivos_con_extension
            else:
                return None
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def file_remove(extension: str, path: str) -> None:
        """Método para eliminar archivos en una ubicación específica.

        :param extension: La extensión o tipo de archivo a eliminar.
        :type extension: str
        :param path: Ruta o ubicación de donde se eliminarán los archivos.
        :type path: str
        """
        try:
            archivos = os.listdir(path)
            archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]
            if archivos_con_extension is not None:
                print("\nEliminando archivos:", end="\n")
                pu.progress_bar(0, len(archivos_con_extension))
                i:int = 0
                for archivo in archivos_con_extension:
                    sleep(0.1)
                    ruta_archivo = os.path.join(path, archivo)
                    os.remove(ruta_archivo)
                    i += 1
                    pu.progress_bar(i,len(archivos_con_extension))

                print(f"\nSe eliminaron {len(archivos_con_extension)} archivos")
            else:
                print("No se encontraron archivos")
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def validar_path(path: str) -> None:
        """Método para validar la existencia de una carpeta. Si no existe, crea la carpeta en la ubicación indicada.

        :param path: Ruta de la carpeta a comprobar su existencia
        :type path: str
        """
        try:
            if not os.path.exists(path):
                os.mkdir(path)
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def load_config():
        """Método para leer el archivo de configuración que contiene la información por default que tendrá en cuenta el simulador.

        :return: Datos default con la información que llevará la simulación.
        :rtype: dict
        """
        try:
            config_path = os.path.join(os.getcwd())
            with open(f"{config_path}\\config.json") as config_file:
                data = json.load(config_file)
            return data
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def load_file(path: str):
        """Método para cargar un archivo

        :param path: ruta absoluta del archivo
        :type path: str
        :return: data que contiene el archivo
        :rtype: any
        """
        try:
            with open(path) as file:
                data = json.load(file)
            return data
        except Exception as error:
            fu.error_format(error)


    @staticmethod
    def move_files_to_backup(ruta_devices: str, ruta_backup: str, simulacion: int):
        """Método para mover los archivos de la carpeta "devices" a la carpeta "backup"

        :param ruta_devices: Ruta o ubicación de la carpeta "devices"
        :type ruta_devices: str
        :param ruta_backup: Ruta o ubicación de la carpeta "backup"
        :type ruta_backup: str
        :param simulacion: Número de simulación ejecutada
        :type simulacion: int
        """
        try:
            files = ArchivosUtil.files_search(".log", ruta_devices)
            if files is not None:
                for file in files:
                    path_origen: str = f"{ruta_devices}\\{file}"
                    path_destino: str = f"{ruta_backup}\\simulacion_{simulacion}"
                    ArchivosUtil.validar_path(path_destino)
                    os.rename(path_origen, f"{path_destino}\\{file}")
        except Exception as error:
            fu.error_format(error)

