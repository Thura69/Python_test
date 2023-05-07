from tkinter import *
import serial.tools.list_ports
import functools
import datetime
import time

ports = serial.tools.list_ports.comports()
seriaObj = serial.Serial()


root = Tk()
screen_width = root.winfo_screenwidth()
root.config(bg='grey')


def initComPort(index):
    currentPort = str(ports[index])
    comPortVar = str(currentPort.split(' ')[0])
    print(comPortVar)
    seriaObj.port = comPortVar
    seriaObj.baudrate = 9600
    seriaObj.open()


# for onePort in ports:
#     comButton = Button(root, text=onePort, font=(
#         'Calibri', 13), height=1, width=45, command=functools.partial(initComPort, index=ports.index(onePort)))
#     comButton.grid(row=ports.index(onePort), column=0)

dataCanvs = Canvas(root, width=screen_width, height=1080, bg='white')
dataCanvs.grid(row=0, column=1)

# vsb = Scrollbar(root, orient='vertical', command=dataCanvs.yview)
# vsb.grid(row=0, column=2, rowspan=100, sticky='ns')

# dataCanvs.config(yscrollcommand=vsb.set)
dataFrame = Frame(dataCanvs, bg='black')
dataCanvs.create_window((10, 0), window=dataFrame, anchor='nw')

now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")


class FuelData:
    def __init__(self, time, type, sale_gallon, sale_liter):
        self.time = time
        self.type = type
        self.sale_gallon = sale_gallon
        self.sale_liter = sale_liter


fuleDataArray = []

fake_fuel_data = [
    {"time": time,
        "type": "002-Octaneron (95)", "sale_gallon": "4.5", "sale_liter": "4.5"},
    {"time": time,
        "type": "002-Octaneron (95)", "sale_gallon": "4.5", "sale_liter": "4.5"},
    {"time": time,
        "type": "002-Octaneron (95)", "sale_gallon": "4.5", "sale_liter": "4.5"},
]


for fake_data in fake_fuel_data:
    person = FuelData(fake_data["time"], fake_data["type"],
                      fake_data["sale_gallon"], fake_data["sale_liter"])
    fuleDataArray.append(person)


Label(dataFrame, text=f"                  Date                                 Fuel Type                Sale Gallon       Sale Liter", font=(
    'Calibri', 18), bg='lightblue', width=200, anchor="nw").pack()

for data in fuleDataArray:
    label_text = f"{data.time}             {data.type}          {data.sale_gallon}                     {data.sale_liter}"

    Label(dataFrame, text=label_text, font=(
        'Calibri', 18), bg='lightblue', width=200, anchor='nw').pack()


while True:
    root.update()
