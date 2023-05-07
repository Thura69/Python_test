import tkinter as tk
from tkinter import ttk


# window
window = tk.Tk()
window.title("Layout")
window.geometry("1980x1080")
window.config(background="white")

# top frame
top_frame = ttk.Frame(window,)
label1 = ttk.Label(top_frame, text="I am one",
                   background="lightblue", anchor="center")
label2 = ttk.Label(top_frame, text="I am two",
                   background="blue", anchor="center")

# middle widget
label3 = ttk.Label(window, text="I am three",
                   background="blue", anchor="center")

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text="I am four",
                   background="blue", anchor="center")
button1 = ttk.Button(bottom_frame, text="Button one")
button2 = ttk.Button(bottom_frame, text="Button two")

# bottom Button frame
bottom_button_frame = ttk.Frame(bottom_frame)
button_bottom_1 = ttk.Button(bottom_button_frame, text="1")
button_bottom_2 = ttk.Button(bottom_button_frame, text="2")
button_bottom_3 = ttk.Button(bottom_button_frame, text="3")


# top layout
label1.pack(fill="both", expand=True, side="left")
label2.pack(fill="both", expand=True, side="left")
top_frame.pack(fill="both", padx=5, pady=5, expand=True)

# middle layout
label3.pack(expand=True, fill="both", padx=5, pady=5)

# bottom layout
label4.pack(side='left', expand=True, fill='both')
button1.pack(side='left', expand=True, fill='both')
button2.pack(side="left", expand=True, fill='both')
bottom_frame.pack(expand=True, padx=5, pady=5, fill='both')

button_bottom_1.pack(side="top", expand=True, fill='both')
button_bottom_2.pack(side='top', expand=True, fill='both')
button_bottom_3.pack(side='top', expand=True, fill='both')
bottom_button_frame.pack(side='left', expand=True, fill='both', padx=5, pady=5)


window.mainloop()
