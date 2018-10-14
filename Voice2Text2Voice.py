import speech_recognition
from gtts import gTTS
from pygame import mixer
import time

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as input:
    speak = ('Speak Something')
    tts = gTTS(text=speak, lang='en')
    tts.save('speak.mp3')
    mixer.init()
    mixer.music.load('speak.mp3')
    mixer.music.play()
    print('Speak Something')
    voice = recognizer.listen(input)
    speak = ('Voice Synchronized')
    tts = gTTS(text=speak, lang='en')
    tts.save('input.mp3')
    mixer.init()
    mixer.music.load('input.mp3')
    mixer.music.play()
    print('Voice Synchronized')

try:
    time.sleep(1)
    speak = ('your voice in text is')
    tts = gTTS(text=speak, lang='en')
    tts.save('output.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()
    text = recognizer.recognize_google(voice)
    print('Your Voice in Text is:')
    print(text)

    time.sleep(1)
    speak = ('Your Voice in my Voice is')
    tts = gTTS(text=speak, lang='en')
    tts.save('yourvoice.mp3')
    mixer.init()
    mixer.music.load('yourvoice.mp3')
    mixer.music.play()
    print('Your Voice in my Voice')
    time.sleep(1)
    speak = str(text)
    tts = gTTS(text=speak, lang='en')
    tts.save('myvoice.mp3')
    mixer.init()
    mixer.music.load('myvoice.mp3')
    mixer.music.play()
    time.sleep(1)

    f1 = open("voice2text.txt", "w")
    f1.write(text)
    f1.close()
    time.sleep(1)
    speak = ('And Your VoiceText is Stored in voice2text file')
    tts = gTTS(text=speak, lang='en')
    tts.save('store.mp3')
    mixer.init()
    mixer.music.load('store.mp3')
    mixer.music.play()
    print("And Your VoiceText is Stored in voice2text file")
    time.sleep(4)

except:
    speak = ("I'm Sorry I didn't get you")
    tts = gTTS(text=speak, lang='en')
    tts.save('sorry.mp3')
    mixer.init()
    mixer.music.load('sorry.mp3')
    mixer.music.play()
    print("I'm Sorry I didn't get you")
    time.sleep(4)


