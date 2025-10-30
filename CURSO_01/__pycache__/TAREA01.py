     import subprocess

def ejecutar_bat(ruta_bat):
    """Ejecuta un archivo .bat y devuelve el resultado.

    Args:
        ruta_bat: La ruta completa al archivo .bat.

    Returns:
        El objeto de resultado de `subprocess.run()`.
    """
    try:
        resultado = subprocess.run([ruta_bat], shell=True, capture_output=True, text=True, check=True)
        return resultado
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el archivo.bat: {e}")
        return None

# Ejemplo de uso
ruta_del_bat = "C:\Users\josea\OneDrive\Documents\BATCH\RESP_FTP_SUP.bat"  # Reemplaza con la ruta real
resultado_ejecucion = ejecutar_bat(ruta_del_bat)

if resultado_ejecucion:
    print("Salida estándar:", resultado_ejecucion.stdout)
    print("Salida de error:", resultado_ejecucion.stderr)
    print("Código de salida:", resultado_ejecucion.returncode)