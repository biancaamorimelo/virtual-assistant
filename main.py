import speech_recognition as sr
import pyttsx3
from falas import *
from random import choice
import wikipedia
from datetime import datetime
import pywhatkit 

# Setando o idioma de busca da fonte para Português
wikipedia.set_lang('pt')

# Inicializando a engine de voz
engine = pyttsx3.init() 

# Setando a velocidade da fala da voz
engine.setProperty('rate', 120)

# Atribuindo a voz disponivel na engine do Pyttxs3 (em ingles) para biblioteca de LeticiaF123 para Português
voices = engine.getProperty('voices') 
for voice in voices:
    engine.setProperty('voice', voice.id)

# Funcao da voz
def reproduz_voz(frase): 
    engine.say(frase)
    engine.runAndWait()

def processar_voz():
    rec = sr.Recognizer() # Função responsavel por reconhecer a fala

    with sr.Microphone() as s: # Fonte que capta o audio da fala e trata o ruido do ambiente
        rec.adjust_for_ambient_noise(s)  # Funcao que ajusta o ruido do ambiente, captando apenas o som da voz no microfone
        while True:
            try:
                voz = rec.listen(s) # Escuta a voz enquanto houver som sendo captado
                entrada = rec.recognize_google(voz, language='pt') #Biblioteca do Google para reconhecer o idioma de fala Portugues
                print(f'Você disse: {entrada}') #Recebe a entrada de voz e printa em forma de texto
                entrada = entrada.lower()
                #reproduz_voz(entrada)

                if entrada == 'oi' or entrada == 'olá':  # Condição para iniciar o diálogo
                    resposta = choice(cumprimentar)
                    print(resposta) 
                    reproduz_voz(resposta)
                
                elif entrada == 'como está' or entrada == 'como vai' or entrada == 'como você está':
                    resposta = choice(como_esta)
                    print(resposta)
                    reproduz_voz(resposta)
                
                elif entrada == 'sim estou bem' or entrada == 'estou bem' or entrada == 'bem':
                    resposta = choice(humano_bem)
                    print(resposta)
                    reproduz_voz(resposta)
                
                elif entrada == 'que horas são' or entrada == 'me diga as horas':
                    now = datetime.now()
                    hora_de_agora = (f'{now.hour}:{now.minute}')
                    print(hora_de_agora)
                    reproduz_voz(hora_de_agora)
                
                elif entrada == 'que dia é hoje' or entrada == 'qual a data de hoje':
                    now = datetime.now()
                    data_de_hoje = (f'{now.day}/{now.month}/{now.year}')
                    print(data_de_hoje)
                    reproduz_voz(data_de_hoje)

                elif 'wikipédia' in entrada:    # Condição para reproduzir conteúdo da busca do Wikipédia
                    termo = entrada.split('wikipédia')
                    termo_da_pesquisa = termo[1]
                    reproduz_voz(f'Pesquisando por {termo[1]} no wikipedia')
                    pesquisa = wikipedia.page(termo_da_pesquisa)
                    reproduz_voz('Achamos a página {pesquisa.title} no wikipedia')
                    reproduz_voz('Agora estamos buscando o conteúdo dela')
                    print(f'Fonte: {pesquisa.url}')
                    reproduz_voz(pesquisa.content)
                
                elif 'youtube' in entrada:
                    termo = entrada.split('youtube')
                    termo_da_pesquisa = termo[1]
                    pywhatkit.playonyt(termo_da_pesquisa)

                elif 'pesquise por' in entrada:
                    termo = entrada.split('pesquise por')
                    termo_da_pesquisa[1]
                    pywhatkit.search(termo_da_pesquisa)

            except sr.UnknownValueError: # Mensagem de erro
                print('Não entendi o que foi dito')
                reproduz_voz('Não entendi o que foi dito')
                pass

assistente_virtual = processar_voz()


