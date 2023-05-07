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

# add data to table
table.insert('', '0', text='Row 1', values=('Data 1', 'Data 2'))
table.insert('', '1', text='Row 2', values=('Data 3', 'Data 4'))
table.insert('', '2', text='Row 3', values=('Data 5', 'Data 6'))

# pack the table widget
table.pack()

# start the main loop
root.mainloop()
