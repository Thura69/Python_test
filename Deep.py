from tkinter import *
import time
root = Tk()


screen_width = root.winfo_screenwidth()

dataCanvs = Canvas(root, bg='white', width=screen_width, height='1080')
dataFrame = Frame(dataCanvs)
dataCanvs.grid(row=0, column=1)
dataCanvs.create_window((10, 0), window=dataFrame, anchor='nw')


label = Label(root, text="Hello, World!", font=(
    "Arial", 16), fg="red", bg="white")

label.pack()

label.config(text="Welcome")

label.config(text="Welcome to Python GUI Programming!")


root.mainloop()
