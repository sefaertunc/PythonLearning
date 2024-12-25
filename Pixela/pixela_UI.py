import tkinter as tk
from Utilities import general_supplier


class PixelaUI:

    def __init__(self):
        self.__supplier = general_supplier.GeneralSupplier()

        self.window = tk.Tk()
        self.window.title("Pixela")
        self.window.geometry("500x300")
        self.window.config(padx=10, pady=10, bg="white")

        # Entry Section - Update Entry
        self.date_entry = tk.Entry(self.window, width=15, highlightthickness=0, bg=self.__supplier.get_color_hex_by_name("beige"), font=("Helvetica", 10))
        self.date_entry.grid(row=0, column=0, padx=3, pady=5, sticky="nsew")
        self.date_entry.insert(0,"Date:YYYYMMDD")
        self.date_entry.focus_set()

        # Entry Section - Delete Entry
        self.duration_entry = tk.Entry(self.window, width=15, highlightthickness=0, bg=self.__supplier.get_color_hex_by_name("beige"), font=("Helvetica", 10))
        self.duration_entry.grid(row=0, column=1, padx=3, pady=5, sticky="nsew")
        self.duration_entry.insert(0,"Duration:00.0 min")

        # Update Button
        self.upgrade_button = tk.Button(
            self.window, height=1, width=12, text="Update", font=("Helvetica", 10),
            highlightthickness=0, bg=self.__supplier.get_color_hex_by_name("green")
        )
        self.upgrade_button.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

        # Delete Button
        self.delete_button = tk.Button(
            self.window, height=1, width=12, text="Delete", font=("Helvetica", 10),
            highlightthickness=0, bg=self.__supplier.get_color_hex_by_name("red")
        )
        self.delete_button.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")

        # Show Graph Button
        self.graph_button = tk.Button(
            self.window, height=1, text="Show Graph", font=("Helvetica", 10),
            highlightthickness=0, bg=self.__supplier.get_color_hex_by_name("cyan")
        )
        self.graph_button.grid(row=2, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")

        # Show Detailed Graph Button
        self.detailed_graph_button = tk.Button(
            self.window, height=1, text="Show Detailed Graph", font=("Helvetica", 10),
            highlightthickness=0, bg=self.__supplier.get_color_hex_by_name("magenta")
        )
        self.detailed_graph_button.grid(row=3, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")

        # Statistics Canvas
        self.stats_canvas = tk.Canvas(self.window, width=200, height=200, bg="lightyellow", highlightthickness=1)
        self.stats_canvas.grid(row=0, column=2, rowspan=4, padx=5, pady=5, sticky="nsew")

        self.stats_canvas.create_text(
            100, 100, text="Statistics", fill="black", font=("Helvetica", 10, "bold")
        )

        # Grid Configuration
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=2)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_rowconfigure(3, weight=1)
