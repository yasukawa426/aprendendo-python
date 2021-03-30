import speech_recognition as sr
import pyaudio
import os
import webbrowser

r = sr.Recognizer() #a classe q vai reconhecer a fala
# ele consegue usar varias APIs para reconhecer. Tds menos a da google precisa de uma chave e senha para usar. O google vem com uma chave ja
# recognize_bing(): Microsoft Bing Speech
# recognize_google(): Google Web Speech API
# recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
# recognize_houndify(): Houndify by SoundHound
# recognize_ibm(): IBM Speech to Text
# recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx.Só esse funciona offline
# recognize_wit(): Wit.ai
mic = sr.Microphone() #instancia um microfone

#carrega o audio de um arquivo e entao reconhece
harvard = sr.AudioFile("audio_files_harvard.wav") #instancia um AudioFile com o arquivo de audio. WAV AIFF AIFF-C FLAC
ola = sr.AudioFile("ola.wav")
imagine = sr.AudioFile("imagine.wav")

with harvard as source:
    audio = r.record(source)
with ola as source:
    audio2 = r.record(source)
with imagine as source:
    audio3 = r.record(source)

with mic as source:
    print("Pode falar")
    audioMic = r.listen(source, phrase_time_limit=5)

pesquisa = (r.recognize_google(audioMic, language= "pt-BR"))

webbrowser.open("https://www.google.com/search?q=" + "+".join(pesquisa.split()), new = 2, autoraise=True)
# print(r.recognize_google(audio))

# print(r.recognize_google(audio2, language= "pt-BR"))

# print(r.recognize_google(audio3, language= "pt-BR")) comentei para n gastar quota

