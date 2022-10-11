# Importing Libraries
from logging import root
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initializing Window metrics
root = Tk()
root.geometry('400x350')
root.configure(bg='white')
root.title("TC's Text-to-Speech")

Label(root, text="TEXT_TO_SPEECH", font="arial 30 bold", bg='white smoke').pack()
Label(text="Text-to-Speech", font='arial 20 bold',
      bg='white smoke', width='20').pack(side='bottom')

Txt = StringVar()
Label(root, text="Enter Text", font='arial 20 bold',
      bg='white smoke').place(x=20, y=60)

entry_field = Entry(root, textvariable='Txt', width='50')
entry_field.place(x=20, y=100)


# # TTS function
# def Text_to_Speech():
#     Msg = entry_field.get()
#     print(type(Msg))
#     speech = gTTS(text=str(Message))
#     speech.save('Textaudio.mp3')
#     playsound('Textaudio.mp3')


# # Exit
# def Exit():
#     root.destroy()


# # Reset
# def reset():
#     Txt.set("")


# # Defining Buttons
# Button(root, text="PLAY", font='arial 20 bold',
#        command=Text_to_Speech, width='4').place(x=25, y=140)
# Button(root, font='arial 20 bold', text='EXIT', width='4',
#        command=Exit, bg='OrangeRed1').place(x=100, y=140)
# Button(root, font='arial 20 bold', text='RESET',
#        width='6', command=reset).place(x=175, y=140)

# root.mainloop()