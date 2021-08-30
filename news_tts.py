import gtts
from playsound import playsound
import os

def voice(news):
    for article in news:
        gtts.gTTS(article, lang='ru').save('header.mp3')
        gtts.gTTS(news[article], lang='ru').save('text.mp3')
        playsound('header.mp3')
        playsound('text.mp3')
        os.remove('header.mp3')
        os.remove('text.mp3')