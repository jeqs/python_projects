import pyttsx3

text_speech = pyttsx3.init()
answer = input("Insert Text to Speech: ")
text_speech.say(answer)
text_speech.runAndWait()
