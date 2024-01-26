# Apolo-11

## Integrantes del equipo

* Esteban Sanchez - esanchezce92@gmail.com
* Elizabeth Alvarez Castro - eliza.ac93@gmail.com
* Juan Camilo Anzola Gomez - juancamil85@gmail.com

## Descripcion General 
 
* Trabajo final nivel 3 y 4 del Bootcamp de Python: Coding Up My Future
 
## Lenguaje de Programacion y Librerias
 
### Lenguaje: 

* Python == 3.10.11

### Librerias:

* Virtualenv == 20.23.0
* pandas == 2.1.3
 
## Sistema Operativo
 
* Sistema: Windows 11 Pro for Workstations
* Version: 10.0.22631 N/D Compilación 22631

## Como usar:

Primero iniciaremos el entorno virtual con el siguiente comando en la terminal estando en la carpeta raiz del proyecto:

* Para Linux o Mac

> source venv/bin/activate

* Para Windows

> .\venv\Scripts\activate

Para asegurarnos de que las librerias necesarias esten instaladas utilizaremos el siguiente comando:

>  pip install -r requirements.txt

Por ultimo, estando en la carpeta raiz, utilizaremos el script Apolo-11.py (puede ser con o sin argumentos):

* Sin argumentos (los parametros estan predefinidos):

> python Apolo-11.py

* Con argumentos (**No es necesario usar todos los argumentos al mismo tiempo**):

> python Apolo-11.py -i 20 -a 100

La lista de argumentos son:

> -i para el intervalo en segundos de la simulacion
>
> -a para la cantidad de archivos que se generaran en la simulacion
>
> -min para la cantidad minima al azar de archivos que se generaran en la simulacion. (Se utiliza en conjunto con el argumento -max)
>
> -max para la cantidad maxima al azar de archivos que se generaran en la simulacion. (Se utiliza en conjunto con el argumento -min)





 