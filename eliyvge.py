from tkinter import *
import random

root=Tk()
root.title("rng word")

root.geometry("400x400")
root.configure(background = 'snow')

list1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

label = Label(root)

def rng():
    rngf = random.randint(0, 25)
    rngf1 = random.randint(0, 25)
    rngf2 = random.randint(0, 25)
    rngf3 = random.randint(0, 25)
    
    rngfrind = list1[rngf]
    rngfrind1 = list1[rngf1]
    rngfrind2 = list1[rngf2]
    rngfrind3 = list1[rngf3]
    
    label["text"] = str(rngfrind + rngfrind1 + rngfrind2 + rngfrind3)
    
btn = Button(root, text = "Random word",command=rng)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx = 0.5,rely=0.6,anchor=CENTER)

root.mainloop()