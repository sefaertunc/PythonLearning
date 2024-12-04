import tkinter as tk
import random as rd
from Utilities import general_supplier
from Utilities import password_generator as pg

supplier = general_supplier.GeneralSupplier()
pass_gen = pg.PasswordGenerator()

FONT_NAME = "Courier"


def generate_password():
	password = pass_gen.random_password(7, 4, 2)
	password_entry.delete(0, tk.END)
	password_entry.insert(0, password)


def add_datas():
	print("In Method")
	if website_entry.get() != "" and email_entry.get() != "" and password_entry.get() != "":
		print("In Condition")
		with open("data.txt", "a") as data_file:
			data_file.write("Sample\n")
	else:
		warning_window = tk.Toplevel()
		warning_window.title("Blank Space Error")
		warning_label = tk.Label(warning_window, text="Please fill in all the fields.", font=(FONT_NAME, 20, "bold"))
		warning_window.minsize(width=300, height=100)
		warning_label.pack()


# region GUI
window = tk.Tk()
window.title('Password Generator GUI')
window.config(padx=20, pady=20)
window.minsize(500, 350)

canvas = tk.Canvas(window, width=500, height=350, highlightthickness=0)
image = tk.PhotoImage(file='logo.png')
canvas.create_image(250, 175, image=image)
canvas.grid(column=1, row=0)

website_label = tk.Label(window, text='Website:', font=(FONT_NAME, 20))
website_label.grid(column=0, row=1)

website_entry = tk.Entry(window, width=50)
website_entry.grid(column=1, row=1)

email_label = tk.Label(window, text='Email:', font=(FONT_NAME, 20))
email_label.grid(column=0, row=2)

email_entry = tk.Entry(window, width=50)
email_entry.grid(column=1, row=2)

password_label = tk.Label(window, text='Password:', font=(FONT_NAME, 20))
password_label.grid(column=0, row=3)

password_entry = tk.Entry(window, width=25)
password_entry.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=48, command=add_datas)
add_button.grid(column=1, row=4)

window.mainloop()

# endregion
