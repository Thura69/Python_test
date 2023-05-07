import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Layout")
window.geometry("1980x1080")
window.config(bg="white")

canvs = tk.Canvas(window, bg="white", scrollregion=(0, 0, 16000, 16000))
canvs.create_line(0, 0, 2000, 5000, fill='green', width=10)

canvs.pack(fill='both', expand=True)
scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvs.yview)
canvs.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

canvs.bind('<MouseWheel>', lambda event: canvs.yview_scroll(
    int(event.delta / 60), "units"))


window.mainloop()
