import speech_recognition as sr

r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US").lower()
        except sr.UnknownValueError:
            pass
        print(text)
        return text


listen()