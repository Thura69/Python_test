import tkinter as tk
from time import strftime


class DigitalClock:
    def __init__(self, master):
        self.master = master
        master.title("Digital Clock")

        self.clock_running = False
        self.time_label = tk.Label(master, font=(
            'calibri', 40, 'bold'), background='black', foreground='green')
        self.time_label.pack(anchor='center', fill='both', expand='yes')

        self.start_button = tk.Button(
            master, text='Start', command=self.start_clock)
        self.start_button.pack(side='left', padx=10)

        self.pause_button = tk.Button(
            master, text='Pause', state='disabled', command=self.pause_clock)
        self.pause_button.pack(side='left')

    def update_time(self):
        self.current_time = strftime('%H:%M:%S %p')
        self.time_label.config(text=self.current_time)

        if self.clock_running:
            self.time_label.after(1000, self.update_time)

    def start_clock(self):
        if not self.clock_running:
            self.clock_running = True
            self.start_button.config(state='disabled')
            self.pause_button.config(state='normal')
            self.update_time()

    def pause_clock(self):
        if self.clock_running:
            self.clock_running = False
            self.start_button.config(state='normal')
            self.pause_button.config(state='disabled')


root = tk.Tk()
clock = DigitalClock(root)
root.geometry("350x150")
root.mainloop()
