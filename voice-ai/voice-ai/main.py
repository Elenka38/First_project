# Голосовой помощник, выводит ответ на экран терминала, открывет сайт (можно указать любой)


import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
# перебираем в цикле наши микрофоны


def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()

sayToMe("Привет всем! У нас все работает отлично")
sayToMe("Скажите хоть что то")

record = sr.Recognizer()
try:
    with sr.Microphone(device_index=0) as source: #микрофон помещаем в переменную source
        print("Говори..")
        audio = record.listen(source)

        result = record.recognize_google(audio, language="ru-Ru")
        result = result.lower()
        print(result)

        if result == "скажи время":
            now = datetime.datetime.now()
            str_date = "Сейчас {}:{}".format(str(now.hour), str(now.minute))
            print(str_date)
            sayToMe(str_date)
        elif result == "открой веб-сайт":
            webbrowser.open("https://google.com")


except sr.UnknownValueError:
    print("Голос не был распознан")
except sr.RequestError:
    print("Что то пошло не так")





