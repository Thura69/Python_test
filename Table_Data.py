from tkinter import *
from datetime import datetime
from tkinter import ttk
root = Tk()


screen_width = root.winfo_screenwidth()


nozzle_one_saleprice = 0
nozzle_one_saleliter = 0

nozzle_two_saleprice = 0
nozzle_two_saleliter = 0

nozzle_three_saleprice = 0
nozzle_three_saleliter = 0

nozzle_four_saleprice = 0
nozzle_four_saleliter = 0


nozzle_one = Label(root,
                   text=f"Nozzle-1  Sale Price:{nozzle_one_saleprice} Total Liter:{nozzle_one_saleliter}", width=100, anchor="nw")
nozzle_two = Label(root,
                   text=f"Nozzle-2  Sale Price:{nozzle_two_saleprice} Total Liter:{nozzle_two_saleliter}", width=100, anchor="nw")
nozzle_three = Label(root,
                     text=f"Nozzle-3  Sale Price:{nozzle_three_saleprice} Total Liter:{nozzle_three_saleliter}", width=100, anchor="nw")
nozzle_four = Label(root,
                    text=f"Nozzle-4  Sale Price:{nozzle_four_saleprice} Total Liter:{nozzle_four_saleliter}", width=100, anchor="nw")

nozzle_one.pack()
nozzle_two.pack()
nozzle_three.pack()
nozzle_four.pack()


i = 0
while i <= 500:
    # update row 1 with new value

    # update root window
    new_value = str(i)

    nozzle_one.config(
        text=f"Nozzle-1  Sale Price:{new_value} Total Liter:{new_value}")

    root.update()

    i += 1


# start the main loop
root.mainloop()
