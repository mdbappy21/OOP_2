from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from abc import ABC, abstractmethod


class BaseCalculator(ABC):
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("510x620+300+200")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f1f5")

        self._initialize_ui()

    @abstractmethod
    def _initialize_ui(self):
        pass

    @abstractmethod
    def calculate_bmi(self):
        pass


class BMICalculator(BaseCalculator):
    def __init__(self, root):
        self.height = tk.DoubleVar()
        self.weight = tk.DoubleVar()
        self.height.set(0)
        self.weight.set(0)
        super().__init__(root)

    def _initialize_ui(self):
        self._setup_icon()
        self._setup_images()
        self._setup_entries()
        self._setup_sliders()
        self._setup_button()
        self._setup_labels()

    def _setup_icon(self):
        image_icon = PhotoImage(file="img/icon.png")
        self.root.iconphoto(False, image_icon)

    def _setup_images(self):
        top = PhotoImage(file="img/top.png")
        top_image = Label(self.root, image=top, background="#f0f1f5")
        top_image.image = top
        top_image.place(x=-10, y=-10)

        box = PhotoImage(file="img/box.png")
        box_label1 = Label(self.root, image=box, bg="#f0f1f5")
        box_label1.image = box
        box_label1.place(x=20, y=100)
        box_label2 = Label(self.root, image=box, bg="#f0f1f5")
        box_label2.image = box
        box_label2.place(x=260, y=100)

        scale = PhotoImage(file="img/scale.png")
        scale_label = Label(self.root, image=scale, bg="#f0f1f5")
        scale_label.image = scale
        scale_label.place(x=20, y=335)

        self.man_image = Label(self.root, bg="#f0f1f5")
        self.man_image.place(x=70, y=530)

    def _setup_entries(self):
        self.height_entry = Entry(self.root, textvariable=self.height, width=6, font="arial 42", bg="#fff", fg="#000",bd=0)
        self.height_entry.place(x=40, y=160)

        self.weight_entry = Entry(self.root, textvariable=self.weight, width=6, font="arial 42", bg="#fff", fg="#000", bd=0)
        self.weight_entry.place(x=275, y=160)

    def _setup_sliders(self):
        style = ttk.Style()
        style.configure("TScale", background="white")

        height_label = Label(self.root, text="Height (cm)", font="arial 10 bold", bg="#f0f1f5", fg="#000")
        height_label.place(x=80, y=220)
        self.height_slider = ttk.Scale(self.root, from_=0, to=220, orient="horizontal", style="TScale", command=self._height_slider_changed, variable=self.height)
        self.height_slider.place(x=70, y=250, width=150)

        weight_label = Label(self.root, text="Weight (kg)", font="arial 10 bold", bg="#f0f1f5", fg="#000")
        weight_label.place(x=300, y=220)
        self.weight_slider = ttk.Scale(self.root, from_=0, to=200, orient="horizontal", style="TScale", command=self._weight_slider_changed, variable=self.weight)
        self.weight_slider.place(x=300, y=250, width=150)

    def _setup_button(self):
        Button(self.root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=self.calculate_bmi).place(x=340, y=340)

    def _setup_labels(self):
        self.bmi_label = Label(self.root, font="arial 50 bold", bg="#f0f1f5", fg="#000")
        self.bmi_label.place(x=125, y=320)

        self.result_label = Label(self.root, font="arial 20 bold", bg="#f0f1f5", fg="#3b3a3a")
        self.result_label.place(x=310, y=400)

        self.comment_label = Label(self.root, font="arial 10 bold", bg="#f0f1f5")
        self.comment_label.place(x=180, y=480)

    def _height_slider_changed(self, event):
        self.height.set(round(self.height_slider.get(), 2))
        self._update_man_image()

    def _weight_slider_changed(self, event):
        self.weight.set(round(self.weight_slider.get(), 2))

    def _update_man_image(self):
        size = int(float(self.height.get()))
        img = Image.open("img/man.png")
        resized_image = img.resize((50, 10 + size))
        photo2 = ImageTk.PhotoImage(resized_image)
        self.man_image.config(image=photo2)
        self.man_image.place(x=70, y=580 - size)
        self.man_image.image = photo2

    def calculate_bmi(self):
        h = self.height.get()
        w = self.weight.get()

        if h == 0:
            self.bmi_label.config(text="Error")
            self.result_label.config(text="Invalid input")
            self.comment_label.config(text="Height cannot be zero")
            return

        m = h / 100
        bmi = round(float(w / m ** 2), 1)
        self.bmi_label.config(text=bmi)

        if bmi <= 18.5:
            self.result_label.config(text="Underweight!")
            self.comment_label.config(text="You have lower weight than normal body! \nPrioritize nutrient-dense foods, increase caloric \nintake, and incorporate resistance training for \nmuscle gain.")
        elif 18.5 < bmi <= 25:
            self.result_label.config(text="Normal!")
            self.comment_label.config(text="You are healthy. Maintain balanced nutrition \nand regular exercise for overall health and \nwell-being.")
        elif 25 < bmi <= 30:
            self.result_label.config(text="Overweight!")
            self.comment_label.config(text="You are slightly overweight! Focus on portion \ncontrol, whole foods, and a combination of \naerobic and strength training exercises.")
        else:
            self.result_label.config(text="Obese!")
            self.comment_label.config(text="Your health is at risk. Advocate for personal-\n-ized dietary plans, structured workouts, and \ncomprehensive support to achieve lasting \nweight control and overall health.")


if __name__ == "__main__":
    root = Tk()
    calculator = BMICalculator(root)
    root.mainloop()
