#GUI Calculator

from tkinter import *

import tkinter.messagebox as a

root = Tk()
root.title("Calculator")
root.geometry('300x300')

def calc():
    
    root2 = Tk()
    root2.title("Operations")
    root2.geometry('500x500')
    
    #Labels
    
    cal = Label(root2,text = "CALCULATOR",font=40,fg="white",bg="black",width=100)
    
    f = Label(root2,text = "First Number")
    
    s = Label(root2,text = "Second Number")
    
    f_n = Entry(root2)
    
    s_n = Entry(root2)
    
    #Positioning
    
    cal.pack()
    
    f.place(x=30,y=120)
    
    s.place(x=30,y=150)
    
    f_n.place(x=150,y=120)
    
    s_n.place(x=150,y=150)

    
    def add():
        total_sum = (int(f_n.get())+int(s_n.get()))
        a.showinfo("Addition",f"Result = {total_sum}")
        root2.destroy()
    
        
    def sub():
        total_sub = (int(f_n.get())-int(s_n.get()))
        a.showinfo("Subtraction",f"Result = {total_sub}")
        root2.destroy()
        
    
    def mul():
        total_mul = (int(f_n.get())*int(s_n.get()))
        a.showinfo("Multiplication",f"Result = {total_mul}")
        root2.destroy()
    
    
    def div():
        total_div = (int(f_n.get())/int(s_n.get()))
        a.showinfo("Multiplication",f"Result = {total_div}")
        root2.destroy()

    
    def clear():
        f_n.delete(0,'end')
        s_n.delete(0,'end')

    #Buttons
    
    add_b = Button(root2,text = "ADD",fg='white',bg='black',width=10,command=add).place(x=30,y=360)
    
    sub_b = Button(root2,text = "Subtract",fg='white',bg='black',width=10,command=sub).place(x=140,y=360)
    
    mul_b = Button(root2,text = "Multiply",fg='white',bg='black',width=10,command=mul).place(x=250,y=360)
    
    div_b = Button(root2,text="Divide",fg="white",bg="black",width=10,command=div).place(x=360,y=360)
    
    clear_b = Button(root2,text = "Clear",fg='white',bg='black',width=10,command=clear).place(x=180,y=460)

butt1 = Button(text = "Calculate",font=30,fg='white',bg='black',command=calc).place(x=110,y=110)

root.mainloop()