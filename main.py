from tkinter import *
import tkinter as tk
import subprocess
import sys
import os

root = tk.Tk()
root.title("Object Oriented Programming || Project")
root.geometry("900x500+300+200")
root.configure(bg='gray')
frame = tk.Frame(root, bg='gray')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def open_bmi():
    try:
        subprocess.Popen([sys.executable, os.path.join(os.getcwd(), 'BMI.py')])
    except Exception as e:
        print(f"Failed to open BMI.py: {e}")


def open_weather():
    try:
        subprocess.Popen([sys.executable, os.path.join(os.getcwd(), 'Weather.py')])
    except Exception as e:
        print(f"Failed to open Weather.py: {e}")


button1 = tk.Button(frame, text="Open BMI Calculator", command=open_bmi, width=20, height=2)
button1.pack(pady=20)
button2 = tk.Button(frame, text="Open Weather App", command=open_weather, width=20, height=2)
button2.pack(pady=20)


root.mainloop()
