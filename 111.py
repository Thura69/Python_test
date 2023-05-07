import tkinter as tk
from tkinter import ttk

# create root window
root = tk.Tk()

# create treeview widget
table = ttk.Treeview(root, columns=('column1', 'column2'))

# set headings for columns
table.heading('#0', text='Row')
table.heading('column1', text='Column 1')
table.heading('column2', text='Column 2')

# add initial data to table
table.insert('', '0', text='Row 1', values=('Data 1', 'Data 2'))
table.insert('', '1', text='Row 2', values=('Data 3', 'Data 4'))
table.insert('', '2', text='Row 3', values=('Data 5', 'Data 6'))

# pack the table widget
table.pack()

# iterate through numbers 0 to 100
i = 0
while i <= 100:
    # update row 1 with new value
    new_value = str(i)
    table.item('0', values=('Data 1', new_value))

    # update root window
    root.update()

    i += 1

# start the main loop
root.mainloop()
