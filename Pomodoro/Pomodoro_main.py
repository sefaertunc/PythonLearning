import tkinter as tk
from tkinter import PhotoImage
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	count_down(1 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	count_sec = count % 60
	count_min = count // 60
	tomato_canvas.itemconfig(timer_text, text=f'{math.floor(count_min):02d}:{count_sec:02d}')
	if count > 0:
		window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
tomato_canvas.create_image(100, 112, image=tomato_image)
timer_text = tomato_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
tomato_canvas.grid(column=1, row=1)

title_label = tk.Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start_button = tk.Button(width=5, text="Start", font=FONT_NAME, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(width=5, text="Reset", font=FONT_NAME, bg=YELLOW)
reset_button.grid(column=2, row=2)

checkmark_text = tk.Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
checkmark_text.grid(column=1, row=3)

window.mainloop()
