from tkinter import *
# here calling the package
window = Tk()
window.geometry("500x700")#window size 

#adding inputs 
menu=Menu(window) #here creating a window like a group 
file=Menu(menu , tearoff=0) 
file.add_command(label="new") #using add_command to add a elements in window 
file.add_command(label="open")
file.add_command(label="save")
file.add_command(label="save as")
file.add_separator() # this add_separate draw the line between theme like categare
file.add_command(label="exit")
menu.add_cascade(label= "menu",menu= file ) #using this to visulize the button to click the menu 
window.config(menu=menu) 

window.title("Frames and Buttons")
window.mainloop()