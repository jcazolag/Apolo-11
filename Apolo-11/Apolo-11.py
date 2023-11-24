import os
import random
from datetime import datetime
import argparse
from dependencies.simulador import Apolo11Simulador


def main():
    #Obtiene la ruta donde se guardan los archivos
    ruta_preferencia = os.path.join(os.getcwd(), "files")

    #Inicializa el objeto del simulador y se le añade la ruta de guardado de archivos
    apolo11_simulador = Apolo11Simulador(ruta_preferencia)
    
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(description='Descripción del script de Apollo-11')

    # Agrega un argumento llamado '-i' que espera un valor entero para definir el intervalo de la simulacion
    parser.add_argument('-i', '--intervalo', type=int, help='Define el intervalo de tiempo de la simulacion en segundos', default=None)

    # Agrega un argumento llamado '-a' que espera un valor de entero para definir la cantidad de archivos en la simulacion
    parser.add_argument('-a', '--archivos', type=int, help='Define la cantidad de archivos que genera la simulacion', default=None)

    # Parsea los argumentos de la línea de comandos
    args = parser.parse_args()

    # Verifica si se proporcionaron valores para los argumentos
    if args.intervalo is not None and args.archivos is not None:
        #ejecuta la simulacion con argumentos de intervalo y archivos dados por el usuario
        apolo11_simulador.ejecutar_simulacion(args.intervalo, args.archivos)

    elif args.intervalo is not None:
        #ejecuta la simulacion con el argumento de intervalo dado por el usuario
        apolo11_simulador.ejecutar_simulacion(intervalo=args.intervalo)

    elif args.archivos is not None:
        #ejecuta la simulacion con el argumento de archivo dado por el usuario
        apolo11_simulador.ejecutar_simulacion(max_archivos=args.archivos)

    else:
        #ejecuta la simulacion sin argumentos dados por el usuario
        apolo11_simulador.ejecutar_simulacion()

if __name__ == "__main__":
    main()
