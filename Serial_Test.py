import serial
import tkinter as tk

# Create a serial object
ser = serial.Serial('COM3', 9600)  # replace with your port and baudrate

# Create a GUI window
window = tk.Tk()

# Create a function to write data to the serial port


def write_data():
    data = entry.get()
    ser.write(data.encode())

# Create a function to read data from the serial port


def read_data():
    data = ser.readline().decode()
    label.config(text=data)


# Create a label to display the received data
label = tk.Label(window, text="")

# Create an entry widget to enter data to send
entry = tk.Entry(window)

# Create a button to send the data
button = tk.Button(window, text="Send", command=write_data)

# Place the widgets in the window
label.pack()
entry.pack()
button.pack()

# Set up a timer to read data from the serial port
window.after(100, read_data)

# Start the GUI event loop
window.mainloop()

# Close the serial port when the program exits
ser.close()
