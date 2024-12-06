import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
BLUE = "#81BFDA"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_pomodoro():
	global reps
	window.after_cancel(timer)
	title_label['text'] = "Timer"
	checkmark_text['text'] = ""
	tomato_canvas.itemconfig(timer_text, text="00:00")
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	global reps
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60
	reps += 1
	if reps % 8 == 0:
		count_down(long_break_sec)
		title_label.config(text="Long Break", fg=BLUE, bg=YELLOW)
		reps = 0
	elif reps % 2 == 0:
		count_down(short_break_sec)
		title_label.config(text="Short Break", fg=GREEN, bg=YELLOW)
	else:
		count_down(work_sec)
		title_label.config(text="Work Time", fg=PINK, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	count_sec = count % 60
	count_min = count // 60
	tomato_canvas.itemconfig(timer_text, text=f'{math.floor(count_min):02d}:{count_sec:02d}')
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		global reps
		print(reps)
		if reps % 2 != 0:
			checkmark_text["text"] += "✔"


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=200, pady=50, bg=YELLOW)
window.minsize(width=600, height=350)

tomato_canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
tomato_canvas.create_image(100, 112, image=tomato_image)
timer_text = tomato_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
tomato_canvas.grid(column=1, row=1)

title_label = tk.Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start_button = tk.Button(width=5, text="Start", font=FONT_NAME, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(width=5, text="Reset", font=FONT_NAME, bg=YELLOW, command=reset_pomodoro)
reset_button.grid(column=2, row=2)

checkmark_text = tk.Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
checkmark_text.grid(column=1, row=3)

window.mainloop()
