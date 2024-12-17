import tkinter as tk
from Utilities import general_supplier

__supplier = general_supplier.GeneralSupplier()
BACKGROUND = __supplier.get_color_hex_by_name("black")


class TriviaUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Trivia Game")
        self.window.geometry("400x600")
        self.window.config(padx=25, pady=25, bg=BACKGROUND)

        # Force the window to show up first
        self.window.wm_attributes("-topmost", True)
        self.window.update()  # Force update to apply the attribute

        # Canvas
        self.question_canvas = tk.Canvas(width=350, height=350, highlightthickness=0, bg="white")
        self.question_canvas.grid(row=2, column=0, columnspan=2, pady=30)
        self.question_canvas_text = self.question_canvas.create_text(
            175, 175, text="Sample Question", width=350, fill="black", font=("Helvetica", 20)
        )

        # Labels
        self.current_score = tk.Label(text="Score:", font=("Helvetica", 15), bg=BACKGROUND, fg="black")
        self.current_score.grid(row=0, column=1)

        self.high_score = tk.Label(text="High Score", font=("Helvetica", 15), bg=BACKGROUND, fg="black")
        self.high_score.grid(row=0, column=0)

        # Buttons with Images
        self.true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(width=100, height=97, highlightthickness=0, image=self.true_image)
        self.true_button.grid(row=3, column=0)

        self.false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(width=100, height=97, highlightthickness=0, image=self.false_image)
        self.false_button.grid(row=3, column=1)
