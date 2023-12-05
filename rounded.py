from tkinter import *


# Create an instance of tkinter frame
root= Tk()

# Set the size of the tkinter window
root.geometry("700x350")

f = Frame(root, width=1000, bg="blue")
f.pack(fill=X, expand=True)

l = Label(f, text="hi", width=10, bg="red", fg="white")
l.pack()

root.mainloop()