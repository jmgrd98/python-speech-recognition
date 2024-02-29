import speech_recognition as sr

rec = sr.Recognizer()

# print(sr.Microphone().list_microphone_names())
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print('Fale agora')
    audio = rec.listen(mic)
    try:
        text = rec.recognize_google(audio, language='pt-BR')
        print(text)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
    except sr.RequestError as e:
        print(f"Erro ao fazer a requisição ao Google Speech Recognition service; {e}")
