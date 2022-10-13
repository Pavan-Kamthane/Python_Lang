from logging.config import listen
import speech_recognition as sr
import pyttsx3
from GoogleNews import GoogleNews

news = GoogleNews()
a = pyttsx3.init()
speak_voice = a.getProperty('voices')
a.setProperty('voice',speak_voice[1].id)
# voice of female put 1 for male put 0
recognizer = sr.Recognizer()

def speak_news():
    with sr.Microphone() as source:
        print("Firstly clearing out the background noises ....")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Tell me the topic for which you want the news...")
        listen_voice = recognizer.listen(source, timeout=1)
        print("Your voice has been recorded")

    try:
        news_txt = recognizer.recognize_google(listen_voice,language='en_US')
        news_txt = news_txt.lower()
        print("You message which you said is : ",format(news_txt))
    except Exception as e:
        print(e)

    if 'headlines' in news_txt:
        a.say("Wait Getting headlines of today for you")
        a.runAndWait()
        news.get_news('Today news')
        news.result()
        b = news.gettext()
        print(*b[1:5],sep=',')

    if 'sports' in news_txt:
        a.say("Wait Getting sports news of today for you")
        a.runAndWait()
        news.get_news('Sports')
        news.result()
        b = news.gettext()
        print(*b[1:5],sep=',')

    if 'tech' in news_txt:
        a.say("Wait Getting Technology news of today for you")
        a.runAndWait()
        news.get_news('Tech')
        news.result()
        b = news.gettext()
        print(*b[1:5],sep=',')

speak_news()
