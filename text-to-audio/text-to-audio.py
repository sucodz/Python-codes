import pyttsx3

speaker = pyttsx3.init()

voices = speaker.getProperty("voices")
print("number of voices", len(voices))
for voice in voices:
    print('\n',voice,'\n')

# i'm choosing the 2nd
# becaucse the 1st one is French
voice_id = voices[1].id
speaker.setProperty('voice', voice_id)

text="This text will be an Audio."
speaker.say(text)
speaker.runAndWait()
