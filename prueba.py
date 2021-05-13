import speech_recognition as sr
import webbrowser
import pyttsx3 as bot
import pyautogui as gui
import os
from os import system

jarvis = bot.init()
jarvis.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
jarvis.setProperty('rate',150)

r = sr.Recognizer() 

def pregunta():
    jarvis.say('¿Quieres buscar otra cosa?')
    jarvis.runAndWait()
    print('Escuchando : ')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    if text.lower()=="yes" or text.lower()=="si":
        jarvis.say('OK, ¿Qué quieres buscar?')
        jarvis.runAndWait()
        return True
    elif text.lower()=="no":
        return False


with sr.Microphone() as source:

    jarvis.say('Bienvenido al asistente virtual creado por Pudú. Mi nombre es Jenny. vamos a empezar. ¿Cuál es tu nombre?')
    jarvis.runAndWait() 
    print('Escuchando nombre : ')
    audio = r.listen(source)
    name = r.recognize_google(audio)
    jarvis.say('Hola' +name+'....¿Qué quieres ver?')
    jarvis.runAndWait() 
 
    while True:        
        print('Escuchando : ')
        audio = r.listen(source)
        try:        
            text = r.recognize_google(audio)
            print('Usted dijo: {}'.format(text))
            if "facebook" in text.lower():
                jarvis.say('Abriendo Facebook')
                jarvis.runAndWait() 
                system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://es-la.facebook.com/' )") 
                
             
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break
            elif "twitter" in text.lower():
                jarvis.say('Abriendo Twitter')
                jarvis.runAndWait()
                system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://twitter.com/?lang=es' )") 
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break
            elif "whatsApp" in text.lower():
                jarvis.say('Abriendo Whatsapp')
                jarvis.runAndWait()
                system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://web.whatsapp.com/' )")   
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break   
            elif "instagram" in text.lower():
                jarvis.say('Abriendo Instagram')
                jarvis.runAndWait()
                system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://www.instagram.com/?hl=es-la' )") 
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break  
            elif "youtube" in text.lower():
                jarvis.say('Abriendo Youtube')
                jarvis.runAndWait()
                system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://www.youtube.com/' )")  
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break   
            elif "spotify" in text.lower():
                jarvis.say('Abriendo Spotify')
                jarvis.runAndWait()
                system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://www.spotify.com/cl/' )") 
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break  
            elif "block" in text.lower():
                os.system("notepad filename.txt")
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break
            
            elif "exit" in text.lower() or "no" in text.lower():
                jarvis.say('Ok, Chao Bebé')
                jarvis.runAndWait() 
                break              
            else:
                jarvis.say('No se pudo abrir la página solicitada')
                jarvis.runAndWait()                      
        except:
            jarvis.say('Lo siento no te escucho, vuelve a intentarlo')
            jarvis.runAndWait()








    


  
