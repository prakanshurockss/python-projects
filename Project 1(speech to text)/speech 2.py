import speech_recognition as sr

r=sr.Recognizer()

audio=sr.AudioFile('C:\Users\welcome\Desktop\project\Project 1(speech to text)')

with audio as source:
    audioData=r.record(source)
type(audioData)
text=r.recognize_google(audioData)
print(text)
