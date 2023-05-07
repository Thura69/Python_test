import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('500x400')
root.title('LL')

option_frame = tk.Frame(root, bg="#c3c3c3")


option_frame.pack(side='left')
option_frame.configure(width=100, height=400)


def hide_indicate():
    home_indicade.configure(bg="#c3c3c3")
    menu_indicade.configure(bg="#c3c3c3")
    contact_indicade.configure(bg="#c3c3c3")
    about_indicade.configure(bg="#c3c3c3")


def indicate(lab, page):
    hide_indicate()
    lab.configure(bg="#158aff")
    deletePage()
    page()


def deletePage():
    for frame in main_frame.winfo_children():
        frame.destroy()


def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='Home Page', font=('Bold'))
    lb.pack()
    home_frame.pack(pady=20)


def menu_page():
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame, text='Menu Page', font=('Bold'))
    lb.pack()
    menu_frame.pack(pady=20)


def contact_page():
    contact_frame = tk.Frame(main_frame)
    lb = tk.Label(contact_frame, text='Contact Page', font=('Bold'))
    lb.pack()
    contact_frame.pack(pady=20)


def about_page():
    about_frame = tk.Frame(main_frame)
    lb = tk.Label(about_frame, text='About Page', font=('Bold'))
    lb.pack()
    about_frame.pack(pady=20)


home_btn = tk. Button(option_frame, text='Home', font=(
    'Bold', 15), fg='#158aff', bd=0, bg="#c3c3c3", command=lambda: indicate(home_indicade, home_page))
home_btn.configure(width=5, height=2)

home_btn.place(x=10, y=50)

home_indicade = tk.Label(option_frame, text="", bg='#c3c3c3')
home_indicade.place(x=3, y=50, width=5, height=45)

menu_btn = tk. Button(option_frame, text='Menu', font=(
    'Bold', 15), fg='#158aff', bd=0, bg="#c3c3c3", command=lambda: indicate(menu_indicade, menu_page))
menu_btn.configure(width=5, height=2)

menu_btn.place(x=10, y=100)
menu_indicade = tk.Label(option_frame, text="", bg='#c3c3c3')
menu_indicade.place(x=3, y=100, width=5, height=45)

contact_btn = tk. Button(option_frame, text='Contact', font=(
    'Bold', 15), fg='#158aff', bd=0, bg="#c3c3c3", command=lambda: indicate(contact_indicade, contact_page))
contact_btn.configure(width=5, height=2)

contact_btn.place(x=10, y=150)
contact_indicade = tk.Label(option_frame, text="", bg='#c3c3c3')
contact_indicade.place(x=3, y=150, width=5, height=45)


about_btn = tk. Button(option_frame, text='About', font=(
    'Bold', 15), fg='#158aff', bd=0, bg="#c3c3c3", command=lambda: indicate(about_indicade, about_page))
about_btn.configure(width=5, height=2)
about_btn.place(x=10, y=200)
about_indicade = tk.Label(option_frame, text="", bg='#c3c3c3')
about_indicade.place(x=3, y=200, width=5, height=45)

main_frame = tk.Frame(
    root, bg="white", highlightcolor='black', highlightthickness=2)

main_frame.pack(side='left')
main_frame.configure(width=500, height=400)


root.mainloop()
