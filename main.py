import speech_recognition as sr
import time


def record_audio(recognizer: sr.Recognizer) -> str | None:
    """
    Records audio from microphone and converts it to text.

    Returns:
        Transcribed text if successful, else None
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Speech recognition service unavailable.")
    return None


def main():
    recognizer = sr.Recognizer()

    print("Say something (say 'exit' to quit)...")
    time.sleep(1)

    while True:
        text = record_audio(recognizer)

        if not text:
            continue

        print(f"Recognized text: {text}")

        if text.lower() == "exit":
            print("Exiting application.")
            break


if __name__ == "__main__":
    main()
