# -*- coding: utf-8 -*-
#instalar o pyaudio  pip install pipwin pelo pipwin e depois instalar usando python -m pipwin pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import pyttsx3
from datetime import datetime, timedelta

from MonitorTemperatura import verificar_temperatura

import webbrowser

if __name__ == "__main__":

    def ouvir_microfone():

        cont = 0

        speak = pyttsx3.init()
        # speak.setProperty('voice', 'portugal')
        speak.setProperty("rate", 280)
        # voices = speak.getProperty('voices')
        # speak.setProperty("voice", voices[0].id)


        #Habilita o microfone para ouvir o usuario
        microfone = sr.Recognizer()

        with sr.Microphone() as source:

            iniciado = 0
            iniciado_temp = 0

            temp = verificar_temperatura()[0]
            hum = verificar_temperatura()[1]

            while True:
                speak.runAndWait() 
                tempoagora = datetime.now()

                                                                                                 
                # iniciação
                if (iniciado == 0):

                    webbrowser.open(f'https://bno23.pythonanywhere.com/monitoramento/Monitoramento ativado/')

                    # speak.say(f"Assistente iniciado e disponível!")
                    # speak.say(f"A temperatura da sala está em {temp} graus celsius e a umidade está em {hum} por cento!")
                    # # speak.say(f"Um novo chamado!")
                    # speak.runAndWait()  
                    iniciado = 1

                    # os.startfile("monitoramento.bat")

                
                # Monitoramento de temperatura
                if float(temp) > float(23.0) and cont in (5, 10, 20, 30, 40, 50) and iniciado_temp < 1:
                    # monitor = verificar_temperatura()
                    # speak.say(f"A sala do Datacenter está em {temp} graus célsius e {hum} por cento de humidade relativa do ar")   
                    webbrowser.open(f'https://bno23.pythonanywhere.com/monitoramento/Atenção risco de colapso no datacenter A Temperatura da sala está em {temp} graus celsius /')
                    iniciado_temp = 1
                
                # Monitoramento de umidade
                if float(hum) > float(70.0) and cont in (5, 10, 20, 30, 40, 50) and iniciado_temp < 1:
                    # monitor = verificar_temperatura()
                    # speak.say(f"A sala do Datacenter está em {temp} graus célsius e {hum} por cento de humidade relativa do ar")   
                    webbrowser.open(f'https://bno23.pythonanywhere.com/monitoramento/Atenção risco de colapso no datacenter A umidade da sala está em {hum} por cento /')
                    iniciado_temp = 1
                
                microfone.adjust_for_ambient_noise(source)              
                try:
                    audio = microfone.listen(source)
                    frase = microfone.recognize_google(audio, language='pt-BR')
                
                    frasemin = frase.lower()

                    if 'assistente qual a temperatura da sala do data center' in frasemin or 'assistente temperatura data center' in frasemin :
                        webbrowser.open(f'https://bno23.pythonanywhere.com/monitoramento/A Temperatura da sala está em {temp} graus celsius e a humidade relativa do ar está em {hum}/')

                    print(frase)
                                
                except LookupError:
                    print(f'1 - Não Entendi {cont}')
                    print(tempoagora)

                except sr.UnknownValueError as e:
                    print(f'2 - Valor Inválido {cont}')
                    print(tempoagora)

                except KeyboardInterrupt:
                    print('keyboard interrupt')
                    print(tempoagora)
                    
                except:
                    print(f'{cont}')
                    print(tempoagora)
                cont +1


    ouvir_microfone()