import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Layout")
window.geometry("1980x1080")
window.config(bg="white")

canvs = tk.Canvas(window, bg="white", scrollregion=(0, 0, 16000, 16000))


canvs.pack(fill='both', expand=True)

# header
header_frame = tk.Frame(canvs, height=200)

home = tk.Label(header_frame, text="HOME")
about = tk.Label(header_frame, text="ABOUT")
contact = tk.Label(header_frame, text="CONTACT US")

home.pack(side='left', fill='both', expand=True)
about.pack(side='left', fill='both', expand=True)
contact.pack(side='left', fill='both', expand=True)
header_frame.pack(side='top', fill='x')

# BODY
# body_frame = tk.Frame(canvs, bg="white")

# body_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)
# First_Frame
first_frame = tk.Frame(canvs, bg="white")
first_frame.pack(side='top', fill='x', expand=True, padx=10, pady=10)


def create_card1(price, liters):
    card1 = tk.Frame(first_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2)

    card1title_label = tk.Label(card1, fg="black", bg='#1289A7', text="Nozzle 1", font=(
        'Arial', 20, 'bold'),)
    card1title_label.pack(pady=10)

    global card1price_label
    card1price_label = tk.Label(card1, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16))
    card1price_label.pack(pady=10)

    global card1liters_label
    card1liters_label = tk.Label(card1, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card1liters_label.pack(pady=10)

    global card1total_liter
    card1total_liter = tk.Label(card1, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card1total_liter.pack(pady=10)

    card1.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card1


def create_card2(price, liters):
    card2 = tk.Frame(first_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2, width=150, height=200)

    card2title_label = tk.Label(card2, fg="black", bg='#1289A7', text="Nozzle 2", font=(
        'Arial', 20, 'bold'),)
    card2title_label.pack(pady=10)

    global card2price_label
    card2price_label = tk.Label(card2, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card2price_label.pack(pady=10)

    global card2liters_label
    card2liters_label = tk.Label(card2, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card2liters_label.pack(pady=10)

    global card2total_liter
    card2total_liter = tk.Label(card2, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card2total_liter.pack(pady=10)

    card2.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card2


def create_card3(price, liters):
    card3 = tk.Frame(first_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2, width=150, height=200)

    card3title_label = tk.Label(card3, fg="black", bg='#1289A7', text="Nozzle 3", font=(
        'Poppins', 20, 'bold'),)
    card3title_label.pack(pady=10)

    global card3price_label
    card3price_label = tk.Label(card3, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card3price_label.pack(pady=10)

    global card3liters_label
    card3liters_label = tk.Label(card3, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card3liters_label.pack(pady=10)

    global card3total_liter
    card3total_liter = tk.Label(card3, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card3total_liter.pack(pady=10)

    card3.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card3


def create_card4(price, liters):
    card4 = tk.Frame(first_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2)

    card4title_label = tk.Label(card4, fg="black", bg='#1289A7', text="Nozzle 4", font=(
        'Arial', 20, 'bold'),)
    card4title_label.pack(pady=10)

    global card4price_label
    card4price_label = tk.Label(card4, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card4price_label.pack(pady=10)

    global card4liters_label
    card4liters_label = tk.Label(card4, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card4liters_label.pack(pady=10)

    global card4total_liter
    card4total_liter = tk.Label(card4, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card4total_liter.pack(pady=10)

    card4.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card4


create_card1("0", "0.000")
create_card2("0", "0.000")
create_card3("0", "0.000")
create_card4("0", "0.000")


second_frame = tk.Frame(canvs, bg='white')
second_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)


def create_card5(price, liters):
    card5 = tk.Frame(second_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2, width=150, height=200)

    card5title_label = tk.Label(card5, fg="black", bg='#1289A7', text="Nozzle 5", font=(
        'Arial', 20, 'bold'),)
    card5title_label.pack(pady=10)

    global card5price_label
    card5price_label = tk.Label(card5, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card5price_label.pack(pady=10)

    global card5liters_label
    card5liters_label = tk.Label(card5, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card5liters_label.pack(pady=10)

    global card5total_liter
    card5total_liter = tk.Label(card5, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card5total_liter.pack(pady=10)

    card5.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card5


def create_card6(price, liters):
    card6 = tk.Frame(second_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2, width=150, height=200)

    card6title_label = tk.Label(card6, fg="black", bg='#1289A7', text="Nozzle 6", font=(
        'Arial', 20, 'bold'),)
    card6title_label.pack(pady=10)

    global card6price_label
    card6price_label = tk.Label(card6, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card6price_label.pack(pady=10)

    global card6liters_label
    card6liters_label = tk.Label(card6, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card6liters_label.pack(pady=10)

    global card6total_liter
    card6total_liter = tk.Label(card6, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card6total_liter.pack(pady=10)

    card6.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card6


def create_card7(price, liters):
    card7 = tk.Frame(second_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2)

    card7title_label = tk.Label(card7, fg="black", bg='#1289A7', text="Nozzle 7", font=(
        'Arial', 20, 'bold'),)
    card7title_label.pack(pady=10)

    global card7price_label
    card7price_label = tk.Label(card7, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card7price_label.pack(pady=10)

    global card7liters_label
    card7liters_label = tk.Label(card7, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card7liters_label.pack(pady=10)

    global card7total_liter
    card7total_liter = tk.Label(card7, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card7total_liter.pack(pady=10)

    card7.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card7


def create_card8(price, liters):
    card8 = tk.Frame(second_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2, width=150, height=200)

    card8title_label = tk.Label(card8, fg="black", bg='#1289A7', text="Nozzle 8", font=(
        'Arial', 20, 'bold'),)
    card8title_label.pack(pady=10)

    global card8price_label
    card8price_label = tk.Label(card8, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card8price_label.pack(pady=10)

    global card8liters_label
    card8liters_label = tk.Label(card8, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card8liters_label.pack(pady=10)

    global card8total_liter
    card8total_liter = tk.Label(card8, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card8total_liter.pack(pady=10)

    card8.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card8


create_card5("0", "0.000")
create_card6("0", "0.000")
create_card7("0", "0.000")
create_card8("0", "0.000")

third_frame = tk.Frame(canvs, bg="white")
third_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)


def create_card9(price, liters):
    card9 = tk.Frame(third_frame, bg='#1289A7', highlightcolor="black",
                     highlightthickness=2, width=150, height=200)

    card9title_label = tk.Label(card9, fg="black", bg='#1289A7', text="Nozzle 9", font=(
        'Arial', 20, 'bold'),)
    card9title_label.pack(pady=10)

    global card9price_label
    card9price_label = tk.Label(card9, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card9price_label.pack(pady=10)

    global card9liters_label
    card9liters_label = tk.Label(card9, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card9liters_label.pack(pady=10)

    global card9total_liter
    card9total_liter = tk.Label(card9, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card9total_liter.pack(pady=10)

    card9.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card9


def create_card10(price, liters):
    card10 = tk.Frame(third_frame, bg='#1289A7', highlightcolor="black",
                      highlightthickness=2, width=150, height=200)

    card10title_label = tk.Label(card10, fg="black", bg='#1289A7', text="Nozzle 10", font=(
        'Arial', 20, 'bold'),)
    card10title_label.pack(pady=10)

    global card10price_label
    card10price_label = tk.Label(card10, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card10price_label.pack(pady=10)

    global card10liters_label
    card10liters_label = tk.Label(card10, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card10liters_label.pack(pady=10)

    global card10total_liter
    card10total_liter = tk.Label(card10, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card10total_liter.pack(pady=10)

    card10.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card10


def create_card11(price, liters):
    card11 = tk.Frame(third_frame, bg='#1289A7', highlightcolor="black",
                      highlightthickness=2, width=150, height=200)

    card11title_label = tk.Label(card11, fg="black", bg='#1289A7', text="Nozzle 11", font=(
        'Arial', 20, 'bold'),)
    card11title_label.pack(pady=10)

    global card11price_label
    card11price_label = tk.Label(card11, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card11price_label.pack(pady=10)

    global card11liters_label
    card11liters_label = tk.Label(card11, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card11liters_label.pack(pady=10)

    global card11total_liter
    card11total_liter = tk.Label(card11, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card11total_liter.pack(pady=10)

    card11.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card11


def create_card12(price, liters):
    card12 = tk.Frame(third_frame, bg='#1289A7', highlightcolor="black",
                      highlightthickness=2, width=150, height=200)

    card12title_label = tk.Label(card12, fg="black", bg='#1289A7', text="Nozzle 12", font=(
        'Arial', 20, 'bold'),)
    card12title_label.pack(pady=10)

    global card12price_label
    card12price_label = tk.Label(card12, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card12price_label.pack(pady=10)

    global card12liters_label
    card12liters_label = tk.Label(card12, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card12liters_label.pack(pady=10)

    global card12total_liter
    card12total_liter = tk.Label(card12, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card12total_liter.pack(pady=10)

    card12.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card12


create_card9("0", "0.000")
create_card10("0", "0.000")
create_card11("0", "0.000")
create_card12("0", "0.000")


fourth_frame = tk.Frame(canvs, bg="white")
fourth_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)


def create_card13(price, liters):
    card13 = tk.Frame(fourth_frame, bg='#1289A7', highlightcolor="black",
                      highlightthickness=2, width=150, height=200)

    card13title_label = tk.Label(card13, fg="black", bg='#1289A7', text="Nozzle 13", font=(
        'Arial', 20, 'bold'),)
    card13title_label.pack(pady=10)

    global card13price_label
    card13price_label = tk.Label(card13, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card13price_label.pack(pady=10)

    global card13liters_label
    card13liters_label = tk.Label(card13, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card13liters_label.pack(pady=10)

    global card9total_liter
    card13total_liter = tk.Label(card13, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card13total_liter.pack(pady=10)

    card13.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card13


def create_card14(price, liters):
    card14 = tk.Frame(fourth_frame, bg='#1289A7', highlightcolor="black",
                      highlightthickness=2, width=150, height=200)

    card14title_label = tk.Label(card14, fg="black", bg='#1289A7', text="Nozzle 14", font=(
        'Arial', 20, 'bold'),)
    card14title_label.pack(pady=10)

    global card14price_label
    card14price_label = tk.Label(card14, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card14price_label.pack(pady=10)

    global card14liters_label
    card14liters_label = tk.Label(card14, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card14liters_label.pack(pady=10)

    global card14total_liter
    card14total_liter = tk.Label(card14, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card14total_liter.pack(pady=10)

    card14.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card14


def create_card15(price, liters):
    card15 = tk.Frame(fourth_frame, bg='#1289A7', highlightcolor="black",
                      highlightthickness=2, width=150, height=200)

    card15title_label = tk.Label(card15, fg="black", bg='#1289A7', text="Nozzle 15", font=(
        'Arial', 20, 'bold'),)
    card15title_label.pack(pady=10)

    global card15price_label
    card15price_label = tk.Label(card15, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card15price_label.pack(pady=10)

    global card15liters_label
    card15liters_label = tk.Label(card15, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card15liters_label.pack(pady=10)

    global card15total_liter
    card15total_liter = tk.Label(card15, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card15total_liter.pack(pady=10)

    card15.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card15


def create_card16(price, liters):
    card16 = tk.Frame(fourth_frame, bg='#1289A7', highlightcolor="black",
                      highlightthickness=2, width=150, height=200)

    card16title_label = tk.Label(card16, fg="black", bg='#1289A7', text="Nozzle 16", font=(
        'Arial', 20, 'bold'),)
    card16title_label.pack(pady=10)

    global card16price_label
    card16price_label = tk.Label(card16, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Price: {price} MMK", font=(
        'Arial', 16), )
    card16price_label.pack(pady=10)

    global card16liters_label
    card16liters_label = tk.Label(card16, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), )
    card16liters_label.pack(pady=10)

    global card16total_liter
    card16total_liter = tk.Label(card16, width=30, fg="black", bg='#1289A7', anchor="w", text=f"Total Liters: {liters} L", font=(
        'Arial', 16), )
    card16total_liter.pack(pady=10)

    card16.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    return card16


create_card13("0", "0.000")
create_card14("0", "0.000")
create_card15("0", "0.000")
create_card16("0", "0.000")


window.mainloop()
