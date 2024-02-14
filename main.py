import speech_recognition as sr
import time

r = sr.Recognizer()


def record_audio():

    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            audio_data = r.recognize_google(audio)
            print(audio_data)

        except sr.UnknownValueError:
            print('Sorry I did not understand it!')

        except sr.RequestError:
            print('Sorry currently not available!')
        if audio_data == 'exit':
            exit()


time.sleep(1)
print('SAY THE THING TOU WANT AS TEXT')
while  1:

    record_audio()

