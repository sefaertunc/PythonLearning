import tkinter as tk
from tkinter import messagebox
from Utilities import general_supplier
from Utilities import password_generator as pg
import saver_mech

supplier = general_supplier.GeneralSupplier()
pass_gen = pg.PasswordGenerator()

FONT_NAME = "Helvetica"
file_path_json = "data.json"
file_path_txt = "data.txt"


def generate_password():
    password = pass_gen.random_password(7, 4, 2)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def search_accounts():
    data = saver_mech.load_data(file_path_json)
    platforms = [datum["platform"] for datum in data["accounts"]]

    if website_entry.get() in platforms:
        account = next((datum for datum in data["accounts"] if datum["platform"] == website_entry.get()), None)

        if account:
            messagebox.showinfo("Account",
                                f"Platform: {account['platform']}\nEmail: {account['email']}\nPassword: {account['password']}")
    else:
        messagebox.showerror("Wrong", "Please enter a valid account platform!")
    clean_entries()


def add_datas():
    if len(website_entry.get()) != 0 and len(email_entry.get()) != 0 and len(password_entry.get()) != 0:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"E-mail: {email_entry.get()}\n Password: {password_entry.get()}\n Are you sure?",
                                       icon="warning")
        if is_ok:
            saver_mech.add_update_json_data(file_path_json, website_entry.get(), email_entry.get(),
                                            password_entry.get())
            saver_mech.add_text_data(file_path_txt, website_entry.get(), email_entry.get(), password_entry.get())
            clean_entries()
    else:
        messagebox.showinfo("Error", "Please fill in all the blanks!")


def clean_entries():
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# region GUI
window = tk.Tk()
window.title('Password Generator GUI')
window.config(padx=20, pady=20)
window.minsize(200, 200)

canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
image = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0, columnspan=3)

website_label = tk.Label(window, text='Website:', font=(FONT_NAME, 15))
website_label.grid(column=0, row=1)

website_entry = tk.Entry(window, width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = tk.Button(window, text='Search', width=14, command=search_accounts,
                          bg=supplier.get_color_hex_by_name("orange"))
search_button.grid(column=2, row=1, columnspan=3)

email_label = tk.Label(window, text='Email:', font=(FONT_NAME, 15))
email_label.grid(column=0, row=2)

email_entry = tk.Entry(window, width=37)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sefaertnc@gmail.com")

password_label = tk.Label(window, text='Password:', font=(FONT_NAME, 15))
password_label.grid(column=0, row=3)

password_entry = tk.Entry(window, width=18)
password_entry.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", command=generate_password,
                            bg=supplier.get_color_hex_by_name("green"))
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=32, command=add_datas, bg=supplier.get_color_hex_by_name("blue"))
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

# endregion
