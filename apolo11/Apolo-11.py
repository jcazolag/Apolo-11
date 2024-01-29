import os
import random
import argparse
from simulador.simulador import Apolo11Simulador
from utilitarios.archivos import ArchivosUtil as au
from utilitarios.formato import FormatoUtil as fu
from utilitarios.menu import MenuUtil


def main():
    """
    Función principal del programa donde se darán los
    comandos para la ejecución de las simulaciones,
    apoyandose en la lectura de parsers para los parámetros
    y valores de la simulación.
    """
    try:
        ruta_preferencia: str = os.path.join(os.getcwd(), "files")
        au.validar_path(ruta_preferencia)

        apolo11_simulador = Apolo11Simulador(ruta_preferencia)

        parser = argparse.ArgumentParser(
            description='Descripción del script de Apollo-11')

        parser.add_argument('-i',
                            '--intervalo',
                            type=int,
                            help='Define el intervalo de tiempo de la' +
                            ' simulacion en segundos',
                            default=None)

        parser.add_argument('-a',
                            '--archivos',
                            type=int,
                            help='Define la cantidad de archivos que genera' +
                            ' la simulacion',
                            default=None)

        parser.add_argument('-min',
                            '--min_archivos',
                            type=int,
                            help='Define la cantidad minima de archivos que' +
                            ' genera la simulacion. ' +
                            'Debe usarse con el argumento "-max"',
                            default=None)

        parser.add_argument('-max',
                            '--max_archivos',
                            type=int,
                            help='Define la cantidad maxima de archivos' +
                            ' que genera la simulacion.' +
                            ' Debe usarse con el argumento "-min"',
                            default=None)

        parser.add_argument('-m',
                            '--menu',
                            type=str,
                            help='Menu de ayuda ' +
                            ' -m open: para abrir el menu',
                            default=None)

        # Parsea los argumentos de la línea de comandos
        args = parser.parse_args()

        if (
            args.intervalo is not None and args.archivos is not None
            and args.min_archivos is None and args.max_archivos is None
            and args.menu is None
        ):
            apolo11_simulador.ejecutar_simulacion(
                abs(args.intervalo),
                abs(args.archivos))
        elif (
            args.intervalo is not None and args.archivos is None
            and args.min_archivos is None and args.max_archivos is None
            and args.menu is None
        ):
            apolo11_simulador.ejecutar_simulacion(
                intervalo=abs(args.intervalo))
        elif (
            args.archivos is not None and args.intervalo is None
            and args.min_archivos is None and args.max_archivos is None
            and args.menu is None
        ):
            apolo11_simulador.ejecutar_simulacion(
                num_archivos=abs(args.archivos))
        elif (
            args.min_archivos is not None or
            args.max_archivos is not None
        ):
            if (
                args.min_archivos is not None and args.max_archivos is None
                or args.min_archivos is None
                and args.max_archivos is not None
                and args.menu is None
            ):
                print(
                    'Los argumentos "-min" y "-max" se ' +
                    'deben usar en conjunto ' +
                    'para determinar al azar la cantidad de archivos ' +
                    'a generar entre "-min" hasta "-max"'
                )
            elif abs(args.min_archivos) > abs(args.max_archivos):
                print(
                    'El argumento "-min" no puede ser ' +
                    'mayor al argumento "-max"'
                )
            elif (
                args.min_archivos is not None
                and args.max_archivos is not None
                and args.archivos is not None
                and args.menu is None
            ):
                print(
                    'El argumento -a no se puede usar ' +
                    'junto con los argumentos "-min" y "-max"'
                )
            else:
                apolo11_simulador.ejecutar_simulacion(
                    num_archivos=random.randint(abs(args.min_archivos),
                                                abs(args.max_archivos)))
        elif (
            args.intervalo is not None and args.archivos is None
            and args.min_archivos is not None
            and args.max_archivos is not None
            and args.menu is None
        ):
            if (abs(args.min_archivos) > abs(args.max_archivos)):
                print(
                    'El argumento "-min" no puede ser ' +
                    'mayor al argumento "-max"'
                )
            else:
                apolo11_simulador.ejecutar_simulacion(
                    intervalo=args.intervalo,
                    num_archivos=random.randint(
                        abs(args.min_archivos),
                        abs(args.max_archivos)))
        elif (
            args.intervalo is not None and args.archivos is None
            and args.min_archivos is not None and args.max_archivos is None
            or args.intervalo is not None and args.archivos is None
            and args.min_archivos is None and args.max_archivos is not None
            and args.menu is None
        ):
            print(
                'Los argumentos "-min" y "-max" se deben usar ' +
                'en conjunto para determinar al azar la cantidad ' +
                'de archivos a generar entre "-min" hasta "-max"'
            )
        elif (
            args.intervalo is None and args.archivos is None
            and args.min_archivos is None and args.max_archivos is None
            and args.menu is not None
        ):
            if args.menu == 'open':
                menu = MenuUtil()
                menu.menu_ppal()
            else:
                print(
                    "El argumneto -m debe usarse solamente con" +
                    " la palabra 'open' (-m open)")
        else:
            apolo11_simulador.ejecutar_simulacion()
            pass
    except Exception as error:
        fu.error_format(error)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        fu.error_format(error)
