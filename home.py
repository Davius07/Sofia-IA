#Importaciones
#descargar pip

import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, keyboard
from pygame import mixer
#del sistema
import colors as colors
import os, time, platform, datetime
import subprocess as sub


# Variables Iniciadas

name = "sofia"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 145)

sites={
    'google' : 'google.com',
    'youtube' : 'youtube.com',
    'facebook' : 'facebook.com',
    'whatsapp' : 'web.whatsapp.com',
    'classroom' : 'classroom.google.com/u/1/h',
}

files={
       
}

programs={
    "navegador" : "Brave.exe",
    "spotify" : "Spotify.exe",
    "whatsapp" : "Whatsapp.exe",
    "discord" : "Discord.exe",
    "editor de codigo" : "code.exe"
}

#Funciones

def clear():
    time.sleep(0)
    if platform.system() == "Windows":
        os.system("cls")
    else:
       os.system("clear") 
clear()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    listener = sr.Recognizer()     
    with sr.Microphone() as source:
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("No te entendí, intenta de nuevo")
        if name in rec:
            rec = rec.replace(name, '')
    return rec

def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk('El archivo fue creado con exito')
    time.sleep(0)
    talk('Ya puedes ver tu archivo')
    sub.Popen("nota.txt", shell=True)

#Funcion Principal
def run_sofia():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo" + music)
            pywhatkit.playonyt(music)
        
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang('es')
            wiki = wikipedia.summary(search, 1)
            print(search +": " + wiki)
            talk(wiki)
        
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk('Alarma activada a las ' + num + 'horas')
            while True:
                if datetime.datetiem.now().strftime('%H:%M') == num:
                    print("Sonando Alarma!")
                    mixer.init()
                    mixer.music.load('media\audios\Alarma001.mp3')
                    mixer.music.play()
                    if keyboard.read_key()=="s":
                        mixer.music.stop()
                        break
                    
        elif 'colores' in rec:
            talk('Enseguida')
            colors.capture()
            
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start brave.exe {sites[site]}', shell=True)
                    talk(f'abriendo {site}')
            for app in programs:
                if app in rec:
                    talk(f"abriendo {app}")
                    os.system(programs[app])
                    
        elif 'archivo' in rec:
            #for archivo in files:
                #if archivo in rec:
                    #sub.Popen([files[archivo]], shell=True)
                    #talk("abriendo")
            talk("Aun no esta activada esta funcion")

        elif 'escribe' in rec:
            try:
                with open('nota.txt', "a") as f:
                    write(f)
                    
            except FileNotFoundError as e:
                file = open("nota.txt", "a")
                write(file)

        elif 'salir' in rec:
            talk('saliendo del sistema')
            break
  
  
  
  
  
        
if __name__ == '__main__':
        run_sofia()