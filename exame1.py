# Importa las bibliotecas necesarias
import os  # Para trabajar con el sistema operativo
import subprocess  # Para ejecutar comandos de shell
import sys  # Para interactuar con el intérprete de Python

# Define una función llamada check_updates
def check_updates():
    # Ejecuta el comando 'yum check-update' y captura su salida estándar y de error
    result = subprocess.run(['yum', 'check-update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Si la salida estándar del comando no está vacía, significa que hay actualizaciones disponibles
    if result.stdout:
        print("Hay actualizaciones disponibles.")
        # Pregunta al usuario si desea instalar las actualizaciones
        answer = input("¿Desea instalar las actualizaciones? (s/n) ")
        # Si el usuario responde 's' o 'S', instala las actualizaciones
        if answer.lower() == 's':
            # Ejecuta el comando 'yum -y update' para instalar las actualizaciones
            subprocess.run(['yum', '-y', 'update'])
        else:
            # Si el usuario responde algo distinto de 's' o 'S', no instala las actualizaciones
            print("Las actualizaciones no se instalarán.")
    else:
        # Si la salida estándar del comando está vacía, significa que no hay actualizaciones disponibles
        print("No hay actualizaciones disponibles.")

# Obtiene el ID de usuario del proceso actual
# Si el ID de usuario no es 0 (lo que significa que el proceso no se está ejecutando como root), termina el script
if os.getuid() != 0:
    print("Este script debe ser ejecutado como root.")
    sys.exit(1)

# Llama a la función check_updates
check_updates()
