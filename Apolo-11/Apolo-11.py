import os
import random
from datetime import datetime
import argparse
from dependencies.simulador import Apolo11Simulador
import dependencies.project_utils as pu


def main():
    try:
        # Obtiene la ruta donde se guardan los archivos
        ruta_preferencia = os.path.join(os.getcwd(), "files")
        pu.ValidarPath(ruta_preferencia)

        # Inicializa el objeto del simulador y se le añade la ruta de guardado de archivos
        apolo11_simulador = Apolo11Simulador(ruta_preferencia)
        
        # Configura el parser de argumentos
        parser = argparse.ArgumentParser(description='Descripción del script de Apollo-11')

        # Agrega un argumento llamado '-i' que espera un valor entero para definir el intervalo de la simulacion
        parser.add_argument('-i', '--intervalo', type=int, help='Define el intervalo de tiempo de la simulacion en segundos', default=None)

        # Agrega un argumento llamado '-a' que espera un valor de entero para definir la cantidad de archivos en la simulacion
        parser.add_argument('-a', '--archivos', type=int, help='Define la cantidad de archivos que genera la simulacion', default=None)

        # Agrega un argumento llamado '-min' que espera un valor de entero para definir la cantidad minima de archivos en la simulacion
        parser.add_argument('-min', '--min_archivos', type=int, help='Define la cantidad minima de archivos que genera la simulacion. Debe usarse con el argumento "-max"', default=None)

        # Agrega un argumento llamado '-max' que espera un valor de entero para definir la cantidad maxima de archivos en la simulacion
        parser.add_argument('-max', '--max_archivos', type=int, help='Define la cantidad maxima de archivos que genera la simulacion. Debe usarse con el argumento "-min"', default=None)

        # Parsea los argumentos de la línea de comandos
        args = parser.parse_args()

        # Verifica si se proporcionaron valores para los argumentos
        if args.intervalo is not None and args.archivos is not None and args.min_archivos is None and args.max_archivos is None:
            #ejecuta la simulacion con argumentos de intervalo y archivos dados por el usuario
            apolo11_simulador.ejecutar_simulacion(abs(args.intervalo), abs(args.archivos))
        elif args.intervalo is not None and args.archivos is None and args.min_archivos is None and args.max_archivos is None:
            #ejecuta la simulacion con el argumento de intervalo dado por el usuario
            apolo11_simulador.ejecutar_simulacion(intervalo=abs(args.intervalo))
        elif args.archivos is not None and args.intervalo is None and args.min_archivos is None and args.max_archivos is None:
            #ejecuta la simulacion con el argumento de archivo dado por el usuario
            apolo11_simulador.ejecutar_simulacion(num_archivos=abs(args.archivos))
        elif args.min_archivos is not None or args.max_archivos is not None:
            if args.min_archivos is not None and args.max_archivos is None or args.min_archivos is None and args.max_archivos is not None:
                print('Los argumentos "-min" y "-max" se deben usar en conjunto para determinar al azar la cantidad de archivos a generar entre "-min" hasta "-max"')
            elif abs(args.min_archivos) > abs(args.max_archivos):
                print('El argumento "-min" no puede ser mayor al argumento "-max"')
            elif args.min_archivos is not None and args.max_archivos is not None and args.archivos is not None:
                print('El argumento -a no se puede usar junto con los argumentos "-min" y "-max"')
            else:
                #ejecuta la simulacion con los argumento minimo de archivo y maximo de archivos dado por el usuario
                apolo11_simulador.ejecutar_simulacion(num_archivos=random.randint(abs(args.min_archivos), abs(args.max_archivos)))
        elif args.intervalo is not None and args.archivos is None and args.min_archivos is not None and args.max_archivos is not None:
            if abs(args.min_archivos) > abs(args.max_archivos):
                print('El argumento "-min" no puede ser mayor al argumento "-max"')
            else:
                #ejecuta la simulacion con los argumento intervalo, minimo de archivo y maximo de archivos dado por el usuario
                apolo11_simulador.ejecutar_simulacion(intervalo=args_intervalo,num_archivos=random.randint(abs(args.min_archivos), abs(args.max_archivos)))
        elif args.intervalo is not None and args.archivos is None and args.min_archivos is not None and args.max_archivos is None or args.intervalo is not None and args.archivos is None and args.min_archivos is None and args.max_archivos is not None:
            print('Los argumentos "-min" y "-max" se deben usar en conjunto para determinar al azar la cantidad de archivos a generar entre "-min" hasta "-max"')
        else:
            #ejecuta la simulacion sin argumentos dados por el usuario
            apolo11_simulador.ejecutar_simulacion()
    except Exception as error:
        print("\nAn error occurred:", type(error).__name__, "-", error)

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("\nAn error occurred:", type(error).__name__, "-", error)