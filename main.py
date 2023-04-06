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
    n = 600000
    root.after(n, check_processes) # 600000
    process_time = {}
    timestamp = {}
    counter = 0
    while (counter + 1) * 1000 <= n:
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        if current_app not in process_time.keys():
            process_time[current_app] = 0
        process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
        counter += 1
    update_data(process_time)


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
