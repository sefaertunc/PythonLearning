import requests

person_data = {
	"name": "Sefa",
	"job": "Programmer"
}

updated_data = {
	"name": "Sedat",
	"job": "Technicians"
}

patched_data = {
	"name": "Mami",
}

#region Functions
# r1 = requests.post("https://reqres.in/api/users", json=person_data)
# print(r1.text)
# r2 = requests.put(f'https://reqres.in/api/users/{r1.json().get("id")}', json=updated_data)
# print(r2.text)
# r3 = requests.patch(f'https://reqres.in/api/users/{r1.json().get("id")}', json=patched_data)
# print(r3.text)
# r4 = requests.get(f'https://reqres.in/api/users/{r1.json().get("id")}')
# print(r4.text)
#endregion



file = {"files": open("../Kanye_Quotes/kanye.png", "rb")}
r1 = requests.post("https://httpbin.org/post", files=file)
print(r1.text)