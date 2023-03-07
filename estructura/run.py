import os, time, platform

cargando=0

def clear():
    time.sleep(0)
    if platform.system() == "Windows":
        os.system("cls")
    else:
       os.system("clear") 
clear()

def iniciando():
    print(f"""
            Descargando archivos


            Por favor espere:     
            {cargando}%
            
    """)

os.system('pip install speech_recognition')
cargando = 16
iniciando()
os.system('pip install pywhatkit')
os.system('pip install tkinter')
cargando = 32
iniciando()
os.system('pip install wikipedia')
os.system('pip install PIL')
cargando = 48
iniciando()
os.system('pip install pywhatkit')
cargando = 64
iniciando()
#os.system('pip install datetime')
os.system('pip install keyboard')
cargando = 80
iniciando()
os.system('pip install pygame')
os.system('pip install tk')
cargando = 100
iniciando()

def iniciando():
    print(f"""
            Descargando archivos


            Por favor espere:     
            {cargando}%
            
    """)