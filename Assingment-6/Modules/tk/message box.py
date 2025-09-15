#step1 : import package tkinter
from tkinter import *
import tkinter.messagebox 

#step2 : gui interaction
window =Tk()

#step3 : adding inputs 
window.title("Simple") #using this place a title name (title)
window.geometry("500x500")
'''
tkinter.messagebox.showinfo( " warning ","the time is run out ")
tkinter.messagebox.askokcancel("instagram","instagram uninstall")
tkinter.messagebox.askyesno("instagram","instagram uninstall")
question = tkinter.messagebox.askquestion(" box ","it is raning outside")
if question== True:
    print(" use rain coat")
else:
    print("please take umbrella atleast")
'''
#message box type 2 
var = StringVar()
ent_var=StringVar()
message = Message(window, textvariable= var ,relief= RAISED , padx=100,pady=100,bg="skyblue" )
print("\n")
print("Enter the value") 
print("\n")
def insert():
    result=ent_var.get()
    var.set(result)

entry= Entry(window,textvariable= ent_var )
button=Button(window,text="ok",width=20 ,command= insert)
message.pack()
entry.pack()
button.pack()


#step4 : main loop 
window.mainloop()

