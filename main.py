from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import tkinter as tk
import datetime

root = tk.Tk()


def update_data(data):
    with open("data.json", "a") as f:
        day


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



# start the infinite loop function
check_processes()

root.mainloop()
