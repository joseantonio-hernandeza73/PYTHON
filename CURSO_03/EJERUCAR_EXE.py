#!/usr/bin/env python

import subprocess
import os

# Ruta al archivo .bat
ruta_bat = r"C:/Users/josea/OneDrive/Documents/BATCH/RESP_FTP_PRIVADO.bat"

# Ejecutar el archivo .bat
try:
    # La opción 'shell=True' es necesaria en Windows para ejecutar archivos .bat directamente.
    # capture_output=True captura la salida estándar y de error.
    # text=True formatea la salida como texto (cadenas) en lugar de bytes.
    resultado = subprocess.run(ruta_bat, shell=True, capture_output=True, text=True, check=True)
    
    print("El archivo .bat se ejecutó correctamente.")
    print("Salida estándar:")
    print(resultado.stdout)
    print("Errores (si los hay):")
    print(resultado.stderr)

except subprocess.CalledProcessError as e:
    print(f"Ocurrió un error al ejecutar el archivo .bat: {e}")
    print("Salida de error:")
    print(e.stderr)
except FileNotFoundError:
    print(f"Error: El archivo no fue encontrado en la ruta especificada: {ruta_bat}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")