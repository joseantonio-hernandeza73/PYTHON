from tqdm import tqdm
import time
import subprocess
import ftplib
import os
ruta = '/ruta/a/tu/directorio'
contenido_actual = os.listdir('.')
print(contenido_actual)
host = "192.168.1.64" # Reemplazar con la IP o nombre de host del servidor
usuario = "ddt_99mx"      # Reemplazar con su nombre de usuario
contraseña = "Vitriol99"   # Reemplazar con su contraseña
LISTA = ["Audios","Clasicos","Ingenieria","Masonicos","Videos"]
# Envuelve el iterable con tqdm
PROGRAMA = "C:/Program Files (x86)/WinSCP/winscp.com"
for item in LISTA: 
    ruta = f'D:/Biblioteca/{item}'
    contenido = os.listdir(ruta)
    #print(contenido)
    for i in contenido:
        var01 = "open \"sftp://ddt_99mx:Vitriol99@tubalcainv/\"  \"put  D:/Biblioteca/"+str(item)+"/"+str(i)  + " /media/ddt_99mx/BETA/Biblioteca/"+str(item)+"/"+ str(i) +'"'
        commando = "C:/Program Files (x86)/WinSCP/winscp.com /command "+ var01
        print(commando)
        os.system(commando)
    for i in tqdm(range(100), desc=f"Procesando : {item}" ): 
        time.sleep(0.05) # Simula una tarea
