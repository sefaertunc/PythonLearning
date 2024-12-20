import os
from dotenv import load_dotenv

load_dotenv("../venv/env")

key = os.getenv("SAMPLE")
print(key)