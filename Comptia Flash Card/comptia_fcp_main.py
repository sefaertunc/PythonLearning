import tkinter as tk
from tkinter import messagebox
import json
import time
import random

# Define the intervals for each box in hours
REVIEW_INTERVALS = {1: 23, 2: 47, 3: 95, 4: 167, 5: 335}

# Categories
CATEGORIES = ["CompTIA ITF+", "CompTIA A+", "CompTIA Net+", "CompTIA Sec+"]

STATE_FILE = "leitner_state.json"
WORDS_FILE = "content.json"
last_action = None  # To track the last action for Undo

try:
	with open(WORDS_FILE, "r", encoding="utf-8") as f:
		CONTENT_LISTS = json.load(f)
except FileNotFoundError:
	CONTENT_LISTS = {
		category: {f"Box{i}": [] for i in range(1, 6)} for category in CATEGORIES
	}
# Load saved button states if available
try:
	with open(STATE_FILE, "r") as f:
		button_states = json.load(f)
except FileNotFoundError:
	button_states = {
		category: {f"Box {i}": {"state": "gray", "last_practice": None} for i in range(1, 6)} for category in CATEGORIES
	}


def save_state():
	"""Save button states to file with indent=4."""
	with open(STATE_FILE, "w") as f:
		json.dump(button_states, f, indent=3)


def save_content():
	"""Save content lists to file with indent=4."""
	with open(WORDS_FILE, "w", encoding="utf-8") as f:
		json.dump(CONTENT_LISTS, f, indent=3)


def update_button_colors():
	"""Update button colors and countdown labels."""
	now = time.time()
	for category in CATEGORIES:
		for box_idx in range(1, 6):
			box_key = f"Box {box_idx}"
			last_practice = button_states[category][box_key]["last_practice"]
			interval_hours = REVIEW_INTERVALS[box_idx]
			countdown_text = ""

			if last_practice:
				last_practice_timestamp = float(last_practice)
				time_left = (last_practice_timestamp + interval_hours * 3600) - now
				if time_left <= 0:
					button_states[category][box_key]["state"] = "green"
					countdown_text = "Ready"
				else:
					button_states[category][box_key]["state"] = "orange"

					days = int(time_left // 86400)
					hours = int((time_left % 86400) // 3600)
					minutes = int((time_left % 3600) // 60)
					seconds = int(time_left % 60)
					countdown_text = f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"

			countdown_labels[category][box_key].config(text=countdown_text)


def reset_state():
	"""Reset the button states without affecting the word lists."""
	confirm = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all buttons?")
	if confirm:
		global button_states, last_action
		last_action = None
		button_states = {
			category: {f"Box {i}": {"state": "gray", "last_practice": None} for i in range(1, 6)} for category in
			CATEGORIES
		}
		save_state()
		update_interface()
		messagebox.showinfo("Reset", "All buttons have been reset.")


def undo_last_action():
	"""Undo the last action (button and/or content movement)."""
	global last_action

	if not last_action:
		messagebox.showwarning("Undo", "No action to undo.")
		return

	confirm = messagebox.askyesno("Confirm Undo", "Are you sure you want to undo the last action?")
	if confirm:
		if "contents" in last_action:
			for content_action in last_action["contents"]:
				content = content_action["content"]
				current_box = content_action["current_box"]
				original_box = content_action["original_box"]
				category = content_action["category"]

				if content in CONTENT_LISTS[category][current_box]:
					CONTENT_LISTS[category][current_box].remove(content)
					CONTENT_LISTS[category][original_box].append(content)
			save_content()

		if "button" in last_action:
			button_action = last_action["button"]
			category = button_action["category"]
			box_key = button_action["box_key"]
			previous_state = button_action["previous_state"]
			previous_last_practice = button_action["previous_last_practice"]

			button_states[category][box_key]["state"] = previous_state
			button_states[category][box_key]["last_practice"] = previous_last_practice

		last_action = None
		save_state()
		update_interface()
		messagebox.showinfo("Undo", "The last action has been undone.")


def show_content(category, box_idx):
	"""Display two different contents sequentially from the selected box."""
	box_key = f"Box{box_idx}"
	if box_key in CONTENT_LISTS[category] and len(CONTENT_LISTS[category][box_key]) >= 2:
		content1, content2 = random.sample(CONTENT_LISTS[category][box_key], 2)

		global last_action
		last_action = {
			"button": {
				"category": category,
				"box_key": f"Box {box_idx}",
				"previous_state": button_states[category][f"Box {box_idx}"]["state"],
				"previous_last_practice": button_states[category][f"Box {box_idx}"]["last_practice"]
			},
			"contents": [
				{
					"category": category,
					"current_box": f"Box{box_idx}",
					"original_box": f"Box{box_idx}",
					"content": content1
				},
				{
					"category": category,
					"current_box": f"Box{box_idx}",
					"original_box": f"Box{box_idx}",
					"content": content2
				}
			]
		}

		def handle_second_popup(action):
			"""Handle the second popup and start the countdown."""
			next_box_key = f"Box{box_idx + 1}" if box_idx < 5 else box_key

			if action == "know":
				CONTENT_LISTS[category][next_box_key].append(content2)
				CONTENT_LISTS[category][box_key].remove(content2)

			button_states[category][f"Box {box_idx}"]["state"] = "orange"
			button_states[category][f"Box {box_idx}"]["last_practice"] = str(time.time())
			save_content()
			save_state()
			second_popup.destroy()
			update_interface()

		def show_second_popup():
			global second_popup
			second_popup = tk.Toplevel(app)
			second_popup.title("Second Content")
			tk.Label(second_popup, text=content2, font=("Arial", 16)).pack(pady=20)
			tk.Button(second_popup, text="I Know", command=lambda: handle_second_popup("know")).pack(side="left",
																									 padx=10, pady=10)
			tk.Button(second_popup, text="Not Know", command=lambda: handle_second_popup("not_know")).pack(side="right",
																										   padx=10,
																										   pady=10)

		def handle_first_popup(action):
			if action == "know":
				next_box_key = f"Box{box_idx + 1}" if box_idx < 5 else box_key
				CONTENT_LISTS[category][next_box_key].append(content1)
				CONTENT_LISTS[category][box_key].remove(content1)
			save_content()
			first_popup.destroy()
			show_second_popup()

		global first_popup
		first_popup = tk.Toplevel(app)
		first_popup.title("First Content")
		tk.Label(first_popup, text=content1, font=("Arial", 16)).pack(pady=20)
		tk.Button(first_popup, text="I Know", command=lambda: handle_first_popup("know")).pack(side="left", padx=10,
																							   pady=10)
		tk.Button(first_popup, text="Not Know", command=lambda: handle_first_popup("not_know")).pack(side="right",
																									 padx=10, pady=10)
	else:
		messagebox.showwarning("No Content", f"Not enough content in {category}, {box_key}.")


def update_interface():
	for category in CATEGORIES:
		for box_idx in range(1, 6):
			box_key = f"Box {box_idx}"
			button = buttons[category][box_key]
			state = button_states[category][box_key]["state"]

			has_content = len(CONTENT_LISTS[category][f"Box{box_idx}"]) > 1

			if not has_content:
				button.config(state="disabled", bg="gray")
			else:
				button.config(state="normal" if state in ["green", "gray"] else "disabled")
				button.config(bg="gray" if state == "gray" else "green" if state == "green" else "orange")


app = tk.Tk()
app.title("Leitner System for CompTIA")
app.geometry("1000x700")

buttons = {}
countdown_labels = {}
for row_idx, category in enumerate(CATEGORIES):
	tk.Label(app, text=category, font=("Arial", 12)).grid(row=row_idx * 2, column=0, padx=10, pady=10, sticky="w")
	buttons[category] = {}
	countdown_labels[category] = {}
	for box_idx in range(1, 6):
		box_key = f"Box {box_idx}"
		button = tk.Button(app, text=box_key, width=12, height=2,
						   command=lambda c=category, idx=box_idx: show_content(c, idx))
		button.grid(row=row_idx * 2, column=box_idx, padx=10, pady=10)
		buttons[category][box_key] = button

		countdown_label = tk.Label(app, text="", font=("Arial", 10))
		countdown_label.grid(row=row_idx * 2 + 1, column=box_idx)
		countdown_labels[category][box_key] = countdown_label

undo_button = tk.Button(app, text="Undo", width=10, command=undo_last_action)
undo_button.grid(row=len(CATEGORIES) * 2, column=2, pady=20)
reset_button = tk.Button(app, text="Reset", width=10, command=reset_state)
reset_button.grid(row=len(CATEGORIES) * 2, column=3, pady=20)


def periodic_update():
	update_button_colors()
	update_interface()
	app.after(1000, periodic_update)


periodic_update()
app.mainloop()
