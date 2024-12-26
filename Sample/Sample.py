import requests as rq
from dotenv import load_dotenv
import os

load_dotenv("../.venv/.env")
domain = "https://pixe.la/v1/users/sefaertnc/graphs/g1/20241226"

header = {
            "X-USER-TOKEN": os.getenv("PIXELA"),
        }

code = 0
while not code == 200:
    response = rq.get(domain, headers=header)
    if response.status_code == 200:
        code = response.status_code
    print(f"{response.status_code}: {code}")
