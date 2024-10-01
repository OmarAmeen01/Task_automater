import subprocess
import os
import tkinter
import sys
import tkinter as tk
from frontend.Dashboard.dashboard import Dashboard
root =tk.Tk()
root.geometry("900x600")
Dashboard(root)
root.mainloop()
# subprocess.run(["start","code"],shell=True)o
# filepath = input("enter the file path")
# url = input("enter your url")
# subprocess.run(['start',"chrome",url], shell=True)
# subprocess.run (["code", filepath], shell=True)
# time.sleep(4)
