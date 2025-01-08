import tkinter
import tkinter as tk
from tkinter import ttk

from selenium.webdriver.common.devtools.v129.dom import highlight_rect


class Ui_MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Coffee Machine")
        self.window.geometry("600x600")
        self.window.resizable(False, False)


        self.coffeeListCanvas = tk.Canvas(self.window, width=400, height=300, highlightthickness=0)
        self.coffeeListCanvas.configure()
        self.coffeeListCanvas.grid(row=0, column=0, padx=10, pady=10)

        c1_background1 = self.coffeeListCanvas.create_rectangle(0, 0, 300, 100, fill="#D6C0B3", outline="")
        c1_text1 = self.coffeeListCanvas.create_text(50,50,text="Espresso", font=("Arial", 20, "bold"), fill="white", anchor="w")
        c1_background2 = self.coffeeListCanvas.create_rectangle(300, 0, 400, 100, fill="#AB886D", outline="")
        c1_text2 = self.coffeeListCanvas.create_text(350, 50, text="$2", font=("Arial", 20, "bold"), fill="white")

        c2_background1 = self.coffeeListCanvas.create_rectangle(0, 100, 300, 200, fill="#AB886D", outline="")
        c2_text1 = self.coffeeListCanvas.create_text(50, 150, text="Cappuccino", font=("Arial", 20, "bold"), fill="white", anchor="w")
        c2_background2 = self.coffeeListCanvas.create_rectangle(300, 100, 400, 200, fill="#D6C0B3", outline="")
        c2_text2 = self.coffeeListCanvas.create_text(350, 150, text="$2", font=("Arial", 20, "bold"), fill="white")

        c3_background1 = self.coffeeListCanvas.create_rectangle(0, 200, 300, 300, fill="#D6C0B3", outline="")
        c3_text1 = self.coffeeListCanvas.create_text(50, 250, text="Latte", font=("Arial", 20, "bold"), fill="white", anchor="w")
        c3_background2 = self.coffeeListCanvas.create_rectangle(300, 200, 400, 300, fill="#AB886D", outline="")
        c3_text2 = self.coffeeListCanvas.create_text(350, 250, text="$2", font=("Arial", 20, "bold"), fill="white")








ui = Ui_MainWindow()
ui.window.mainloop()