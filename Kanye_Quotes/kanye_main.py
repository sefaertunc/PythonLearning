import requests as rq
import tkinter as tk


def get_quote():
    response = rq.get("https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()["quote"]
    bg_canvas.itemconfig(quote_text,text=quote)


window = tk.Tk()
window.title("Kanye Quotes")
window.geometry("400x650")
window.config(padx=50, pady=50)

bg_canvas = tk.Canvas(window, width=300, height=414)
bg_image = tk.PhotoImage(file="kanye_background.png")
bg_canvas.create_image(150,207,image=bg_image)
bg_canvas.grid(row=0, column=0)

quote_text = bg_canvas.create_text(150,207,text="Hello Kanyer!!", width=250,font=("Comic Sans MS", 20 ,"bold"))

kanye_image = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button()
kanye_button.config(image=kanye_image, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()