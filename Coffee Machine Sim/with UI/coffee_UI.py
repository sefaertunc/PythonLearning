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
        self.coffeeListCanvas.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        c1_background1 = self.coffeeListCanvas.create_rectangle(0, 0, 300, 100, fill="#D1BB9E", outline="")
        c1_text1 = self.coffeeListCanvas.create_text(50, 50, text="Espresso", font=("Arial", 20, "bold"),
                                                     fill="#493628", anchor="w")
        c1_background2 = self.coffeeListCanvas.create_rectangle(300, 0, 400, 100, fill="#EAD8C0", outline="")
        c1_text2 = self.coffeeListCanvas.create_text(350, 50, text="$2", font=("Arial", 20, "bold"), fill="#493628")

        self.coffeeListCanvas.create_rectangle(0, 100, 300, 200, fill="#EAD8C0", outline="")
        self.coffeeListCanvas.create_text(50, 150, text="Cappuccino", font=("Arial", 20, "bold"), fill="#493628",
                                          anchor="w")
        self.coffeeListCanvas.create_rectangle(300, 100, 400, 200, fill="#D1BB9E", outline="")
        self.coffeeListCanvas.create_text(350, 150, text="$2", font=("Arial", 20, "bold"), fill="#493628")

        self.coffeeListCanvas.create_rectangle(0, 200, 300, 300, fill="#D1BB9E", outline="")
        self.coffeeListCanvas.create_text(50, 250, text="Latte", font=("Arial", 20, "bold"), fill="#493628", anchor="w")
        self.coffeeListCanvas.create_rectangle(300, 200, 400, 300, fill="#EAD8C0", outline="")
        self.coffeeListCanvas.create_text(350, 250, text="$2", font=("Arial", 20, "bold"), fill="#493628")

        self.monitor = tk.Canvas(self.window, width=400, height=200, highlightthickness=0, bg="lightgreen")
        self.monitor.grid(row=1, column=0, columnspan=2)
        self.monitor.create_text(200, 100, text="Monitor", font=("Arial", 20, "bold"), fill="#1F4529", anchor="center")

        self.coffeeSource = tk.Canvas(self.window, width=170, height=200, highlightthickness=0, bg="grey")
        self.coffeeSource.grid(row=1, column=2)
        self.cf = tk.PhotoImage(file="./images/latte.png")
        self.cf_main = self.coffeeSource.create_image(85, 100, image=self.cf)
        self.coffeeSource.tag_bind(self.cf_main, "<Button-1>",
                                   lambda event: self.cleanSource(event, self.coffeeSource, self.cf_main,
                                                                  "delete_image"))

        self.change_P = tk.Canvas(self.window, width=185, height=60, highlightthickness=0, bg="grey")
        self.change_P.grid(row=2, column=0, pady=5)
        self.change_PText = self.change_P.create_text(90, 30, text="Change P", font=("Arial", 12, "bold"),
                                                      fill="#1F4529", anchor="center")
        self.change_P.tag_bind(self.change_PText, "<Button-1>",
                               lambda event: self.cleanSource(event, self.change_P, self.change_PText, "delete_text"))

        self.change_C = tk.Canvas(self.window, width=185, height=60, highlightthickness=0, bg="grey")
        self.change_C.grid(row=2, column=1, pady=5)
        self.change_CText = self.change_C.create_text(90, 30, text="Change C", font=("Arial", 12, "bold"), fill="#1F4529", anchor="center")
        self.change_C.tag_bind(self.change_CText, "<Button-1>",
                              lambda event: self.cleanSource(event, self.change_C, self.change_CText, "delete_text"))

        self.reportButton = tk.Button(self.window, width=23, height=3, background="lightblue", text="Report")
        self.reportButton.grid(row=2, column=2, pady=5, padx=5)

    def cleanSource(self, event, source, element, tag):
        """Tags: delete_image, delete_text"""
        if tag == "delete_image":
            source.delete(element)
        elif tag == "delete_text":
            source.itemconfig(element, text="")


ui = Ui_MainWindow()
ui.window.mainloop()
