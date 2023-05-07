import tkinter as tk

# create a function to update the card values


def update_card(card, total_price, sale_liters):
    # update the card values
    card.itemconfig(total_price_text, text=f"Total Price: {total_price}")
    card.itemconfig(sale_liters_text, text=f"Sale Liters: {sale_liters}")


# create the tkinter window and canvas
root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# create the cards
card_1 = canvas.create_rectangle(
    10, 10, 190, 110, fill="white", outline="black")
card_1_title = canvas.create_text(100, 30, text="Nozzle 1", font=("Arial", 16))
total_price_text = canvas.create_text(
    100, 60, text="Total Price: ", font=("Arial", 12))
sale_liters_text = canvas.create_text(
    100, 80, text="Sale Liters: ", font=("Arial", 12))

card_2 = canvas.create_rectangle(
    10, 120, 190, 220, fill="white", outline="black")
card_2_title = canvas.create_text(
    100, 140, text="Nozzle 1", font=("Arial", 16))
total_price_text_2 = canvas.create_text(
    100, 170, text="Total Price: ", font=("Arial", 12))
sale_liters_text_2 = canvas.create_text(
    100, 190, text="Sale Liters: ", font=("Arial", 12))

card_3 = canvas.create_rectangle(
    10, 230, 190, 330, fill="white", outline="black")
card_3_title = canvas.create_text(
    100, 250, text="Nozzle 2", font=("Arial", 16))
total_price_text_3 = canvas.create_text(
    100, 280, text="Total Price: ", font=("Arial", 12))
sale_liters_text_3 = canvas.create_text(
    100, 300, text="Sale Liters: ", font=("Arial", 12))

card_4 = canvas.create_rectangle(
    10, 340, 190, 440, fill="white", outline="black")
card_4_title = canvas.create_text(
    100, 360, text="Nozzle 2", font=("Arial", 16))
total_price_text_4 = canvas.create_text(
    100, 390, text="Total Price: ", font=("Arial", 12))
sale_liters_text_4 = canvas.create_text(
    100, 410, text="Sale Liters: ", font=("Arial", 12))

# update the card values using the update_card function
update_card(canvas, total_price_text, sale_liters_text)
update_card(canvas, total_price_text_2, sale_liters_text_2)
update_card(canvas, total_price_text_3, sale_liters_text_3)
update_card(canvas, total_price_text_4, sale_liters_text_4)

root.mainloop()
