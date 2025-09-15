from tkinter import *
# here calling the package
window = Tk()
window.geometry("500x700")#window size 
window.config(bg="grey")#window colour 
frame1=Frame(window , bg="red" , width= 200 ,height= 300 , cursor= "dot" )
frame2=Frame(window , bg="white" , width= 200 ,height= 300 , cursor= "DOTBOX")
button1=Button(frame1 , text="button" , bg="black",fg="white")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
window.title("Frames and Buttons")
window.mainloop()