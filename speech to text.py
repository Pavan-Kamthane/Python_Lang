from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
from PIL import ImageTk, Image
from gtts import gTTS
import speech_recognition as sr
import os

root= Tk()
root.title(' Automatic-Notes-Maker')
root.geometry('500x500')
root.resizable(0, 0)
root.configure(bg='light blue')
text1=''
file_name =("E:/minor project/record2.wav")
def recordvoice():
    while True:
        text1 =''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio)
                print(text1)
                txt_area .insert(END, " ")
            except:
                pass
            return text1
def Filevoice():
    while True:
        file_name=filedialog.askopenfilename()
        text1 =''
        r = sr.Recognizer()
        with sr.AudioFile(file_name) as source: # open file 
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio)
                print(text1)
                txt_area .insert(END, " ")
                
            except:
                pass
            return text1           
def Reset():
    txt_area.delete(1.0,END)            

 
def savefile():
    save_text = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    

    if save_text:

        text_area_text = txt_area.get('1.0', 'end-1c')
        
        save_text.write(text_area_text)
        save_text.close()

'''path3="E:/minor project/images/i5.png"
img1 = ImageTk.PhotoImage(Image.open(path3))
lebel_1=Label(root,bd=0,image=img1)
lebel_1.place(x=170,y=90)'''

button_icon1=PhotoImage(file="E:/minor project/images/i5.png")
root.iconphoto(False,button_icon1)

button_icon2=PhotoImage(file="E:/minor project/images/import.png")
root.iconphoto(False,button_icon2)

image_icon3=PhotoImage(file="E:/minor project/images/res1.png")
root.iconphoto(False,image_icon3)
d_btn=Button(root,text='Reset',compound=LEFT,width=170,font='arial 20 bold ',image=image_icon3,relief=SUNKEN,bg='white',activebackground='Gold',bd=10,command=Reset)
d_btn.place(x=140,y=300)

txt_area = Text(root, font=('times new rommon',15,'bold'), height=3, width=25)
txt_area.place(x=120, y=200)
            
recordbutton = Button(root,compound=LEFT,width=100 ,font='arial 9 bold',text='Recording', bg='#9B755F',image=button_icon1,activebackground="gold", command=lambda: txt_area .insert(END, recordvoice()))
recordbutton.place(x=50, y=50)
filebutton = Button(root,compound=LEFT,width=100 ,font='arial 10 bold',text='IMport', bg='#9B755F',image=button_icon2,activebackground="gold", command=lambda: txt_area .insert(END, Filevoice()))
filebutton.place(x=300, y=50)
 
Label(root, text=' automatic notes maker ',font="arial 20", bg='gold').place(x=110, y=0)
 
save_button = Button(root, text='save', font="arial 25", bg='light green', command=lambda: savefile())
save_button.place(x=200, y=400)
 
root.update()
root.mainloop()
