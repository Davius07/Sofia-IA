#Importaciones
#descargar pip
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, keyboard
from pygame import mixer

#del sistema

import colors
import os, time, platform, datetime
import subprocess as sub
from tkinter import *
from PIL import Image, ImageTk
import threading as tr


# Variables Iniciadas
#variables de interfas gui
numero_de_version = str("v2.3.5")
color_de_fondo = "#ffe0ff"
color_de_momento = "#89004f"


#Ventana
main_window= Tk()
main_window.title(f'Sofia - IA  [{numero_de_version}] ')
main_window.geometry('800x400')
main_window.resizable(0,0)
main_window.configure(bg="#ffe0ff")




#variables de funcionalidad

comandos="""\n\n\n\n\n\n\n
    Comandos
    
    - Reproduce
    
    - Busca
    
    - Alarma
    
    - Colores
    
    - Abre
    
    - Archivo
    
    - Escribe

    - Salir o Termina
"""
name = "sofia"
listener = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 145)

sites=dict()

files=dict()

programs=dict()

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

def clock(rec):
    num = rec.replace('alarma', '')
    num = num.strip()
    talk('Alarma activada a las ' + num + 'horas')
    if num[0] != '0' and len (num) < 5:
        num = "0" + num
    print(num)
    while True:
        if datetime.datetiem.now().strftime('%H:%M') == num:
            print("Sonando Alarma!")
            mixer.init()
            mixer.music.load(r'media\audios\alarma.mp3')
            mixer.music.play()
        else:
            continue
        if keyboard.read_key()=="s":
            mixer.music.stop()
            break
        
#Funciones de la GUI
def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)
    
def read_and_talk():
    text = text_info.get("1.0", "end")
    talk(text)

def open_w_pages():
    windows_pages = Toplevel()
    windows_pages.title("Archivos de Paginas   |  Sofia - IA")
    windows_pages.configure(bg=color_de_fondo)
    windows_pages.geometry("300x200")

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
            talk(wiki)
            write_text(search +": " + wiki)
            break
        elif 'alarma' in rec:
            t=tr.Thread(target=clock, args=(rec, ))
            t.start()
                
        elif 'colores' in rec:
            talk('Enseguida')
            colors.capture
            
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

        elif 'salir' or 'termina' in rec:
            talk('saliendo del sistema')
            break

#GUI

#variables de archivos
titulo_photo = ImageTk.PhotoImage(Image.open(r"Titulo.png"))
sofia_photo = ImageTk.PhotoImage(Image.open(r"Sofia.png"))
iniciar_photo = ImageTk.PhotoImage(Image.open(r"Iniciar.png"))
leer_photo = ImageTk.PhotoImage(Image.open(r"Leer Texto.png"))
apps_photo = ImageTk.PhotoImage(Image.open(r"apps.png"))
pages_photo = ImageTk.PhotoImage(Image.open(r"paginas.png"))

#Titulo
label_title = Label(main_window, image=titulo_photo, bg=color_de_fondo, border=0, relief=FLAT)
label_title.pack(pady=5)

label_sofia = Label(main_window, image=sofia_photo, bg=color_de_fondo, border=0, relief=FLAT)
label_sofia.pack(pady=5)

button_iniciar = Button(main_window, image=iniciar_photo, bg=color_de_fondo, border=0, 
                        relief=FLAT, cursor="hand2", command=run_sofia)
button_iniciar.pack(pady=5)

canvas_comandos = Canvas(bg=color_de_fondo, height=270, width=200, bd=0, relief=FLAT)
canvas_comandos.place(x=30, y=10)
canvas_comandos.create_text(90, 80, text=comandos, fill="black", font="Arial 10")

text_info = Text(main_window, bg="#ffa8d9", relief=FLAT, bd=3, fg='black', borderwidth=15)
text_info.place(x=590, y=10, height=270, width=200,)

button_leer = Button(main_window, image=leer_photo, bg=color_de_fondo, border=0, 
                    relief=FLAT, cursor="hand2", command=read_and_talk)
button_leer.place(x=10, y=300)

button_pages = Button(main_window, image=pages_photo, bg=color_de_fondo, border=0, 
                    relief=FLAT, cursor="hand2", command=open_w_pages)
button_pages.place(x=220, y=300)

button_apps = Button(main_window, image=apps_photo, bg=color_de_fondo, border=0, 
                    relief=FLAT, cursor="hand2", command=open_w_apps)
button_apps.place(x=430, y=300)


#Iniciador loop de la ventana
main_window.mainloop()