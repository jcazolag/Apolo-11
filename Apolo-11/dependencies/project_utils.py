import os
import pandas as pd
from time import sleep

# Funcion de barra de progreso para dar una ayuda visual en la consola al usuario
def progress_bar(progress, total):
    percent = 100 * (progress/float(total))
    bar = '█' * int(percent) + '-' * (100-int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress==total:
        print(f"\r|{bar}| {percent:.2f}%", end="\r\n\n")

# Funcion para buscar archivos con una extension especifica en una carpeta dada
def files_search(extension, path):
    try:
        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(path)

        # Filtrar archivos por la extensión deseada
        archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]

        # Verificar si hay archivos con la extensión especificada
        if archivos_con_extension:
            return archivos_con_extension
        else:
            return None
    except Exception as error:
        ErrorFormat(error)

# Funcion para eliminar archivos con una extension especifica en una carpeta dada
def file_remove(extension, path):
    try:
        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(path)

        # Filtrar archivos por la extensión deseada
        archivos_con_extension = [archivo for archivo in archivos if archivo.endswith(extension)]
        if archivos_con_extension is not None:
            print("\nEliminando archivos:", end="\n")
            progress_bar(0, len(archivos_con_extension))
            i = 0
            # Eliminar cada archivo con la extensión especificada
            for archivo in archivos_con_extension:
                sleep(0.1)
                ruta_archivo = os.path.join(path, archivo)
                os.remove(ruta_archivo)
                #print(f"Archivo eliminado: {archivo}")
                i+=1
                progress_bar(i,len(archivos_con_extension))

            print(f"\nSe eliminaron {len(archivos_con_extension)} archivos")
        else:
            print("No se encontraron archivos")
    except Exception as error:
        ErrorFormat(error)
        

# Función para obtener la data de los archivos y devolverlos en un dict
def ObtenerData(ruta_preferencia):
    try:
        data: dict = []
        files = files_search(".log", ruta_preferencia)
        if files is not None:
            for file in files:
                path = f"{ruta_preferencia}\{file}"
                df = pd.read_csv(path, sep=";")
                list_items = df.to_dict(orient='records')
                item = list_items[0]
                data.append(item)
            print(data) 
    except Exception as error:
        ErrorFormat(error)

# Funcion para validar que una carpeta exista, en caso de que no, se crea
def ValidarPath(path: str):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except Exception as error:
        ErrorFormat(error)

# Función para imprimir los errores de las excepciones
def ErrorFormat(error: Exception):
    print("\nAn error occurred:", type(error).__name__, "-", error)