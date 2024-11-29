import tkinter as tk


def calculator():
	try:
		mile = user_input.get()
		km = float(mile) * 1.60934
		result["text"] = f"{km:.2f}"
	except ValueError:
		window2 = tk.Tk()
		window2.title("Error")
		window2.minsize(width=250, height=150)
		error_message = tk.Label(window2, text="ERROR\nEnter a number", font=("Helvetica", 25, "bold"), fg="red")
		error_message.place(x=35, y=50)
		close_button = tk.Button(window2, text="Close", font=("Helvetica", 15), command=window2.destroy)
		close_button.place(x=90, y=120)


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=150)

user_input = tk.Entry(window, width=5)
user_input.focus()
user_input.place(x=150, y=40)

static_word1 = tk.Label(window, text="Miles", font=("Helvetica", 15))
static_word1.place(x=210, y=42)

static_word2 = tk.Label(window, text="is equal to", font=("Helvetica", 15))
static_word2.place(x=70, y=70)

result = tk.Label(window, text="...", font=("Helvetica", 15, "bold"))
result.place(x=155, y=70)

static_word3 = tk.Label(window, text="Km", font=("Helvetica", 15))
static_word3.place(x=210, y=70)

ok_button = tk.Button(window, text="Convert", font=("Helvetica", 15), command=calculator)
ok_button.place(x=135, y=100)

window.mainloop()
