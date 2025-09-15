from tkinter import *
# here calling the package
window = Tk()
window.geometry("500x700")#window size 
button =Button(window , text= "LOGIN" ,fg="red",bg="white",activeforeground="blue" ,activebackground="black",width=8,font=("bold",12))
button.pack()
window.title("Frames and Buttons")
window.mainloop()