from tkinter import *
import time
from datetime import datetime
from tkinter import ttk
root = Tk()


screen_width = root.winfo_screenwidth()

dataCanvs = Canvas(root, width=screen_width, height=1080, bg='white')
dataCanvs.grid(row=0, column=1)
dataFrame = Frame(dataCanvs, bg='black')
dataCanvs.create_window((10, 0), window=dataFrame, anchor='nw')

# create a label with an initial text


class Fueldata():
    def __init__(self, time, fuel_type, sale_gallon, sale_liter):
        self.time = time
        self.fuel_type = fuel_type
        self.sale_gallon = sale_gallon
        self.sale_liter = sale_liter


fuel_data_array = []
nozzle_one_array = []

Label(dataFrame, text=f"Date          Fuel Type        Sale Gallon    Sale Liter", font=(
    'Calibri', 18), bg='lightblue', width=100, anchor="nw").pack()


def updateList():
    for data in fuel_data_array:
        label_text = f"{data.time}             {data.fuel_type}             {data.sale_gallon}                       {data.sale_liter}"
        Label(dataFrame, text=label_text, fg="black",
              bg="lightblue", width=100, anchor="nw", font=("Arial", 18)).pack()

    for data in nozzle_one_array:
        label_text = f"{data.time}             {data.fuel_type}             {data.sale_gallon}                       {data.sale_liter}"
        Label(dataFrame, text=label_text, fg="black",
              bg="lightblue", width=100, anchor="nw", font=("Arial", 18)).pack()


def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    global time
    time = current_time
    root.after(1000, update_time)


update_time()

for_nozzle_one = Label(dataFrame, fg="black",
                       bg="lightblue", width=100, anchor="nw", font=("Arial", 18))

for_nozzle_two = Label(dataFrame, fg="black",
                       bg="lightblue", width=100, anchor="nw", font=("Arial", 18))

for_nozzle_three = Label(dataFrame, fg="black",
                         bg="lightblue", width=100, anchor="nw", font=("Arial", 18))

for_nozzle_four = Label(dataFrame, fg="black",
                        bg="lightblue", width=100, anchor="nw", font=("Arial", 18))

for_nozzle_one.pack()
for_nozzle_two.pack()
for_nozzle_three.pack()
for_nozzle_four.pack()


def fun():
    while True:
        nozzel_no = input("type nozzle no")
        fule_type = input("type fuel type: ")
        sale_gallon = input("type sale gallon: ")
        sale_liter = input("type sale liter: ")

        if nozzel_no == "1":
            for_nozzle_one.config(
                text=f"{time}             {fule_type}             {sale_gallon}                       {sale_liter}")

        elif nozzel_no == "2":
            for_nozzle_two.config(
                text=f"{time}             {fule_type}             {sale_gallon}                       {sale_liter}")

        elif nozzel_no == "3":
            for_nozzle_three.config(
                text=f"{time}             {fule_type}             {sale_gallon}                       {sale_liter}")
        elif nozzel_no == "4":
            for_nozzle_four.config(
                text=f"{time}             {fule_type}             {sale_gallon}                       {sale_liter}")


fun()
root.update()
root.mainloop()
root.geometry("1980*1080")
