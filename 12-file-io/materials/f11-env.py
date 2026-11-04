import os
from dotenv import load_dotenv
load_dotenv()
key = os.environ["API_KEY"]
print("讀到金鑰，長度", len(key))
