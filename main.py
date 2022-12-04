from gtts import gTTS
import os

work = input("Do you want to convert a text into audio? Type 'y' "
             "if you want or type 'n' if you want to exit this program.\n").lower()
if work == "y":
    print("Hello! This program helps to convert text into audio.\n")
    choice= input("Choose how to convert text into audio. Type 'in' if you "
        "want to type text here or 'open' if you want to convert a file.\n").lower()
    if choice == 'in':
        text = input("Type the text here:\n")
    elif choice == 'open':
        file = input("Type the name of a file with '.txt' in the end. \n")
        text = open(file, "r").read().replace("\n", " ")
    else:
        print("Okay, I see, you don't want to continue. Bye!")
    language = input("Choose the language:\n")
    audio = gTTS(text = text, lang = language, slow = False)
    name = input("Choose the name for the audio file. Don't forget to "
            "type '.mp3' at the end! \n")
    audio.save(name)
    os.system(f'start {name}')
elif work == "n":
    print("Okay, bye!")
else:
    print("Well, you've typed something unpredictable. Bye!")
