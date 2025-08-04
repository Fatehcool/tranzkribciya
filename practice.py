from googletrans import Translator
import random
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

duration = 5  # секунды записи
sample_rate = 44100

test = ['привет','пока','машина','молоко','яблоко','мама','папа','игрушка','еда','апельсин']


print("Говори...")
recording = sd.rec(
  int(duration * sample_rate), # длительность записи в сэмплах
  samplerate=sample_rate,      # частота дискретизации
  channels=1,                  # 1 — это моно
  dtype="int16")               # формат аудиоданных
sd.wait()  # ждём завершения записи

wav.write("output.wav", sample_rate, recording)
print("Запись завершена, теперь распознаём...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
try:    
        question = input('Привет ты попал на обучалку по английскому языку, Теперь мне надо узнать какой ты по английскому - начинающий,ученик,носитель  напиши здесьヅ')
        if question == 'Начинающий':
            for i in range(5):
                 random_difficult = random.choice(test)
            print(random_difficult)
            print('Теперь произнеси то что услышал')
            print("Говори...")
            recording = sd.rec(
                int(duration * sample_rate), # длительность записи в сэмплах
                samplerate=sample_rate,      # частота дискретизации
                channels=1,                  # 1 — это моно
                dtype="int16")               # формат аудиоданных
            sd.wait()  # ждём завершения записи
            if random_difficult == recording:
                text = recognizer.recognize_google(audio, language="ru-RU")
                print("Ты сказал:", text)
                translator = Translator()
                translated = translator.translate(text, dest='en')
                print("🌍 Перевод на английский:", translated.text)
                print('Теперь произнеси то что услышал')
                print("Говори...")
                recording2 = sd.rec(
                    int(duration * sample_rate), # длительность записи в сэмплах
                    samplerate=sample_rate,      # частота дискретизации
                    channels=1,                  # 1 — это моно
                    dtype="int16")               # формат аудиоданных
                sd.wait()  # ждём завершения записи
                if recording2 == random_difficult:
                     print('''
                        ┈┈┈┈┈┈▕▔╲┈┈┈┈┈┈
                    ┈┈┈┈     ┈┈┈▏▕┈ⓈⓊⓅⒺⓇ
                    ┈┈┈┈┈     ┈┈▏▕▂▂▂┈┈┈
                    ▂▂▂▂▂▂╱┈▕▂▂▂▏┈┈
                    ▉▉▉▉▉┈┈┈▕▂▂▂▏┈┈
                    ▉▉▉▉▉┈┈┈▕▂▂▂▏┈┈
                    ▔▔▔▔▔▔╲▕▂▂▂▏┈┈
                                ______
                                            ''')
            

except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
    print("Не удалось распознать речь.")
except sr.RequestError as e:             # - если нет интернета или API недоступен
    print(f"Ошибка сервиса: {e}")
