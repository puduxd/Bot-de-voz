import speech_recognition as sr
import webbrowser
import pyttsx3 as bot
import pyautogui as gui
import os


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
    if text.lower()=="yes":
        jarvis.say('OK, ¿Qué quieres buscar?')
        jarvis.runAndWait()
        return True
    elif text.lower()=="no":
        return False


with sr.Microphone() as source:
    jarvis.say('Hola Ezequiel, ¿Qué quieres ver?')
    jarvis.runAndWait() 
 
    while True:        
        print('Escuchando : ')
        audio = r.listen(source)
        try:        
            text = r.recognize_google(audio)
            print('Usted dijo: {}'.format(text))
            if text.lower()=="facebook":
                jarvis.say('Abriendo Facebook')
                jarvis.runAndWait() 
                webbrowser.open("http://www.facebook.com", new=2, autoraise=True)    
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break
            elif text.lower()=="twitter":
                jarvis.say('Abriendo Twitter')
                jarvis.runAndWait()
                webbrowser.open("http://www.twitter.com", new=2, autoraise=True)
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break
            elif text.lower()=="whatsApp":
                jarvis.say('Abriendo Whatsapp')
                jarvis.runAndWait()
                webbrowser.open("https://web.whatsapp.com/", new=2, autoraise=True)   
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break   
            elif text.lower()=="instagram":
                jarvis.say('Abriendo Instagram')
                jarvis.runAndWait()
                webbrowser.open("https://www.instagram.com/?hl=es-la", new=2, autoraise=True)   
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break  
            elif text.lower()=="youtube":
                jarvis.say('Abriendo Youtube')
                jarvis.runAndWait()
                webbrowser.open("https://www.youtube.com/", new=2, autoraise=True)   
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break   
            elif text.lower()=="spotify":
                jarvis.say('Abriendo Spotify')
                jarvis.runAndWait()
                webbrowser.open("https://www.spotify.com/cl/home/", new=2, autoraise=True)   
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break  
            elif text.lower()=="block":
                os.system("notepad filename.txt")
                if pregunta()==True:                          
                    continue
                else: 
                    jarvis.say('Ok, hasta pronto bebé')
                    jarvis.runAndWait() 
                    break
            
            elif text.lower()=="exit":
                jarvis.say('Ok, Chao Bebé')
                jarvis.runAndWait() 
                break              
            else:
                jarvis.say('No se pudo abrir la página solicitada')
                jarvis.runAndWait()                      
        except:
            jarvis.say('Lo siento no te escucho, vuelve a intentarlo')
            jarvis.runAndWait()








    


  
