#step1 : import package tkinter
from tkinter import *

#step2 : gui interaction
window =Tk()

#step3 : adding inputs 
window.title("Simple") #using this place a title name (title)
window.geometry("500x700")  #using this define default size of window (size of window)
window.config(bg="grey")
imp =Label(window,text="Hello World")
imp.pack()

#step4 : main loop 
window.mainloop()

