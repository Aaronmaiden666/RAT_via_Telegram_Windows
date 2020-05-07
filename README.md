````
  ╔═══╦═══╦════╗        ╔════╗ ╔╗                ╔╗╔╗╔╗     ╔╗
  ║╔═╗║╔═╗║╔╗╔╗║        ║╔╗╔╗║ ║║                ║║║║║║     ║║
  ║╚═╝║║ ║╠╝║║╚╝╔╗╔╦╦══╗╚╝║║╠╩═╣║╔══╦══╦═╦══╦╗╔╗ ║║║║║╠╦═╗╔═╝╠══╦╗╔╗╔╦══╗
  ║╔╗╔╣╚═╝║ ║║  ║╚╝╠╣╔╗║  ║║║║═╣║║║═╣╔╗║╔╣╔╗║╚╝║ ║╚╝╚╝╠╣╔╗╣╔╗║╔╗║╚╝╚╝║══╣
  ║║║╚╣╔═╗║ ║║  ╚╗╔╣║╔╗║  ║║║║═╣╚╣║═╣╚╝║║║╔╗║║║║ ╚╗╔╗╔╣║║║║╚╝║╚╝╠╗╔╗╔╬══║
  ╚╝╚═╩╝ ╚╝ ╚╝   ╚╝╚╩╝╚╝  ╚╝╚══╩═╩══╩═╗╠╝╚╝╚╩╩╩╝  ╚╝╚╝╚╩╝╚╩══╩══╝╚╝╚╝╚══╝
                                    ╔═╝║                 
                                    ╚══╝               beta 0.4.45
````
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3572A5.svg)](https://github.com/SebastianEPH)


__Nota:__ Éste proyecto tiene como finalidad el aprendizaje de ciberseguridad y hacking, no me hago responsable de un posible mal uso de ésta herramienta

[Read this documentation in English](Doc/English.md)

# Información Importante
* __Fecha de documentación :__ `07/05/2020`
* __Peso compilado:__ `43MB` aproximadamente
* __Versión Python:__ `3.7` (Obligatoriamente debe ser ésta versión)
## Archivos del repositorio - Github 
![Archivos](https://i.imgur.com/fvVMi8N.png)
- `icon.ico`    = Icono Windows Defender
- `KeyloggerWindows.py` = Código fuente del Keylogger
- `LICENCE` = Licencia 
- `README.md`= Documentación
- `InfoKey.md` = Documentación: Recoleccion de registro de teclas.
- `StartUp.reg` = Modifica el Registro de Windows
- `version.txt` = Información detalla de conversión `.py` a `.exe`
- `WindowsDefender.exe` = Keylogger Compilado 

# Requerimientos de espacio de trabajo
Librerías utilizadas
* __import__ `os` <== API windows
* __import__ `telepot`
* __import__ `requests`
* __import__ `image`
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
* __import__ ``
* __import__ ``
* __import__ ``
* __import__ ``
* __import__ ``
* __import__ ``



# Caracteristicas

# instalación:
## Conversión de `*.py a *.exe`:
## Método de infección:
___¿Cómo infecto a la victima?___

![Final files](https://i.imgur.com/7GJz3De.png)
- Usten tendrá al finalizar 2 archivos:
- El archivo llamado `WindowsDefender.exe` es el keylogger.
- El archivo llamado , modifica el registro de windows, y hace que el keylogger se ejecute siempre al iniciar el usuario.

# Procedimiento de infección:
- Usten guardará esos archivos en un USB
- Es necesario desactivar el antivirus o agregar una exclusión en al siguiente ruta: `"C:\Users\Public\Security\Windows Defender"`
- Lo siguiente es ejecutar el archivo `WindowsDefender.exe` en el USB, el keylogger se replicará en la siguiente ruta `"C:\Users\Public\Security\Windows Defender"`, Se recomienda no sacar el USB al instante ya que el keylogger se estará replicando enla ruta.
- Lo siguiente es darle 2 click al archiv `StartUp.reg`, y ésto hará que el registro de windows sea modificado y el keylogger se ejecute 
- __Nota:__ No hay un orden fijo, usted puede ejecutar primero el archivo `WindowsDefender.exe` cómo el archivo `StartUp.reg` y  ésto no causará ningún problema.

---
# Creador 
* __Repositorio Original:__ [mvrozanti](https://github.com/mvrozanti/RAT-via-Telegram) <== Es el creador original de éste repositorio.
* __Repostitorio:__ [Keylogger_Python](https://github.com/SebastianEPH/Keylogger_Python) <== Éste repositorio fue integrado en su totalidad dentro de [RAT_via_Telegram_Windows](https://github.com/SebastianEPH/RAT_via_Telegram_Windows).
## By SebastianEPH
- [Github](https://github.com/SebastianEPH)
- [Facebook](https://www.facebook.com/SebastianEPH)
- [Linkedin](https://www.linkedin.com/in/sebastianeph/)
- [Telegram](https://t.me/sebastianeph)