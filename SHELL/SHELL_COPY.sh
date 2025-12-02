#!/bin/bash
# Se inicia el respaldo de los archivos de FTP
PAUSA="------------------------------------------------------------>" 
PROYECTO="/media/ddt_99mx/BETA/"
COPI_PROYECTO="/media/ddt_99mx/ETHA/"
ARCHIVO_LOG="/home/ddt_99mx/LOG_COPIA_RESP.txt"
CARPETAS="BODEGA FILOSOFICOS IMAGENES PRIVADO"
echo "Inicia la copia de Respaldo" > $ARCHIVO_LOG
echo $PAUSA >> $ARCHIVO_LOG
FECHA_INI=$(date)
for nombre in $CARPETAS; do
  cp -r $PROYECTO$nombre $COPI_PROYECTO >> $ARCHIVO_LOG
  echo $PAUSA >> $ARCHIVO_LOG
done
FECHA_FIN=$(date)
echo $PAUSA >> $ARCHIVO_LOG
echo " INICIO el Proceso : " $FECHA_INI >> $ARCHIVO_LOG
echo " TERMINO el Proceso : " $FECHA_FIN >> $ARCHIVO_LOG
echo " FIN DEL PROCESO " $FECHA_FIN >> $ARCHIVO_LOG


