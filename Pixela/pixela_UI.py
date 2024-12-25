import tkinter as tk
from Utilities import general_supplier

class PixelaUI:

    def __init__(self):
        self.__supplier = general_supplier.GeneralSupplier()
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Pixela")
        self.window.geometry("450x350")
        self.window.config(padx=50, pady=50)

        date_entry = tk.Entry(self.window, width=30, highlightthickness=0, background=self.__supplier.get_color_hex_by_name("beige"))
        date_entry.grid(row=0, column=0)
        date_entry.focus_set()


        self.window.mainloop()