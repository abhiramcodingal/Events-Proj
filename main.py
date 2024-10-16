# Importing libraries
from tkinter import *
from tkinter import messagebox

# Creating and setting up the screen
root = Tk()
root.geometry("400x300")
root.title("Inches to cm converter")
root.configure(bg="green2")

# Creating command(s)
def show_cm():
    cm = float(in_text.get()) * 2.54
    cm_text.delete(1.0, END)
    cm_text.insert(END, cm)
    
# Creating heading
lbl1 = Label(master=root, text="Length converter", bg="medium blue", fg="gray99", relief="groove", width=54)
lbl1.place(x=10, y=10)

# Creating the frame to keep widgets
frame1 = Frame(master=root, bg="MediumOrchid2", width=380, height=100, relief="raised")
frame1.place(x=10, y=45)

# Creating widgets inside the frame
in_text = Text(master=frame1, bg="aquamarine", fg="yellow4", width=15, height=1, relief="solid")
in_text.place(x=20, y=10)

in_lbl = Label(master=frame1, text="Inches", bg="sienna1", fg="gray99", relief="ridge", width=10)
in_lbl.place(x=160, y=10)

cm_text = Text(master=frame1, bg="aquamarine", fg="yellow4", width=15, height=1, relief="solid")
cm_text.place(x=20, y=60)

cm_lbl = Label(master=frame1, text="Centimetres", bg="sienna1", fg="gray99", relief="ridge", width=10)
cm_lbl.place(x=160, y=60)

ok_btn = Button(master=frame1, text="OK", command=show_cm, bg="dark green", fg="gray99", relief="ridge", width=5)
ok_btn.place(x=230, y=30)

root.mainloop()