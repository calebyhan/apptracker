from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import tkinter as tk
from tkinter import ttk
import datetime
import json

root = tk.Tk()


def update_data(data):
    f = json.load(open("data.json"))
    today = datetime.date.today().strftime("%d-%m-%Y")
    if today not in f:
        f[today] = data
    else:
        f[today] = {i: f[today].get(i, 0) + data.get(i, 0) for i in set(f[today]).union(data)}
    with open("data.json", "w") as file:
        json.dump(f, file)


def check_processes():
    process = {}
    timestamp = {}
    current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    timestamp[current_app] = int(time.time())
    process[current_app] = 1
    update_data(process)
    print(process)
    root.after(1000, check_processes)


root.title("Graph Viewer")

sidebar_frame = ttk.Frame(root, width=200, padding=10)
sidebar_frame.pack(side="left", fill="y")

date_label = ttk.Label(sidebar_frame, text="Select a date:")
date_label.pack()
date_var = tk.StringVar()
date_dropdown = ttk.Combobox(sidebar_frame, textvariable=date_var, values=[])
date_dropdown.pack()

value_label = ttk.Label(root, text="0")
value_label.pack()

check_processes()

root.mainloop()
