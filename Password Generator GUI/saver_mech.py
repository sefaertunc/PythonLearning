import json


# region JSON
def load_data(file_path):
	try:
		with open(file_path, "r") as file:
			return json.load(file)
	except FileNotFoundError:
		return {"accounts": []}  # Return an empty structure if the file doesn't exist


# Function to save JSON data
def save_data(file_path, data):
	with open(file_path, "w") as file:
		json.dump(data, file, indent=4)


# Function to add a new account
def add_json_data(file_path, platform, email, password):
	data = load_data(file_path)
	new_account = {
		"platform": platform,
		"email": email,
		"password": password
	}
	data["accounts"].append(new_account)
	save_data(file_path, data)


# endregion

# region TXT
def add_text_data(file_path_txt, website, email, password):
	with open(f"{file_path_txt}", "a") as data_file:
		data_file.write(f"{website} | {email} | {password}\n")
# endregion
