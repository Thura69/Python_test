import tkinter as tk
# create root window
root = tk.Tk()
# create canvas widget
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
              root.winfo_screenheight()))  # Set window size to full screen
root.configure(bg="white")  # Set background color to white
# Set the window to be full-screen
# create frame to hold cards
frame = tk.Frame(root, background='white')
frame.pack(fill=tk.BOTH, expand=True)
# define card colors
colors = ['lightblue', 'lightblue', 'lightblue', 'lightblue']
# define card texts
titles = ['Nozzle 1', 'Nozzle 2', 'Nozzle 3', 'Nozzle 4']
# create card frames


def create_card1(price, liters):
    card1 = tk.Frame(frame, bg=colors[0], width=150, height=200,
                     highlightbackground="black", highlightthickness=2)
    card1title_label = tk.Label(card1, text=titles[0], font=(
        'Arial', 16), fg='white', bg=colors[0])
    card1title_label.pack(pady=10)
    global card1price_label
    card1price_label = tk.Label(card1, width=30, text=f"Total Price: {price} USD", font=(
        'Arial', 16), fg='white', bg=colors[0])
    card1price_label.pack(pady=10)
    global card1liters_label
    card1liters_label = tk.Label(card1, width=30, text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), fg='white', bg=colors[0])
    card1liters_label.pack(pady=10)
    card1.pack(pady=10,)
    return card1


def create_card2(price, liters):
    card2 = tk.Frame(frame, bg=colors[1], width=150, height=200,
                     highlightbackground="black", highlightthickness=2)
    card2title_label = tk.Label(card2, text=titles[1], font=(
        'Arial', 16), fg='white', bg=colors[1])
    card2title_label.pack(pady=10)
    global card2price_label
    card2price_label = tk.Label(card2, width=30, text=f"Total Price: {price} USD", font=(
        'Arial', 16), fg='white', bg=colors[1])
    card2price_label.pack(pady=10)
    global card2liters_label
    card2liters_label = tk.Label(card2, width=30, text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), fg='white', bg=colors[1])
    card2liters_label.pack(pady=10)
    card2.pack(pady=10)
    return card2


def create_card3(price, liters):
    card3 = tk.Frame(frame, bg=colors[2], width=150, height=200,
                     highlightbackground="black", highlightthickness=2)
    card3title_label = tk.Label(card3, text=titles[2], font=(
        'Arial', 16), fg='white', bg=colors[2])
    card3title_label.pack(pady=10)
    global card3price_label
    card3price_label = tk.Label(card3, width=30, text=f"Total Price: {price} USD", font=(
        'Arial', 16), fg='white', bg=colors[2])
    card3price_label.pack(pady=10)
    global card3liters_label
    card3liters_label = tk.Label(card3, width=30, text=f"Sale Liters: {liters} L", font=(
        'Arial', 16), fg='white', bg=colors[2])
    card3liters_label.pack(pady=10)
    card3.pack(pady=10)
    return card3


def create_card4(price, liters):
    card4 = tk.Frame(frame, bg=colors[3], width=150, height=200,
                     highlightbackground="black", highlightthickness=2)
    card4title_label = tk.Label(card4, text=titles[3], font=(
        'Arial', 16), fg='white', bg=colors[3])
    card4title_label.pack(pady=10)
    global card4_price_label
    card4_price_label = tk.Label(card4, font=(
        'Arial', 16), fg='white', width=30, bg=colors[2])
    card4_price_label.pack(pady=10)
    card4_price_label.config(text=f"Total Price: {price} USD")
    global card4_liters_label
    card4_liters_label = tk.Label(card4, font=(
        'Arial', 16), width=30, fg='white', bg=colors[2])
    card4_liters_label.pack(pady=10)
    card4_liters_label.config(text=f"Sale Liters: {liters} L")
    card4.pack(pady=10)
    return card4


card4 = create_card4("loading..", "loading..")
card3 = create_card3("loading..", "loading..")
card1 = create_card1("loading..", "loading..")
card2 = create_card2("loading..", "loading..")
card1.place(x=30, y=30)
card2.place(x=400, y=30)
card3.place(x=770, y=30)
card4.place(x=1140, y=30)
i = 0
while i <= 1000:
    # update row 1 with new value
    new_value = str(i)
    card4_price_label.config(text=f"Total Price: {new_value} MMK")
    card4_liters_label.config(text=f"Sale Liters: {new_value} L")
    card1liters_label.config(text=f"Sale Liters: {new_value} L")
    card1price_label.config(text=f"Total Price: {new_value} MMK")
    card3liters_label.config(text=f"Sale Liters: {new_value} L")
    card3price_label.config(text=f"Total Price: {new_value} MMK")
    card2price_label.config(text=f"Total Price: {new_value} MMK")
    card2liters_label.config(text=f"Sale Liters: {new_value} L")
    # update root window
    root.update()
    i += 1
root.mainloop()
