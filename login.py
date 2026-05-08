from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")

kite = KiteConnect(api_key=api_key)

print("\nOpen this URL in browser:\n")
print(kite.login_url())

print("\nAfter login copy request_token from browser URL\n")

request_token = input("Enter request token: ")

data = kite.generate_session(
    request_token,
    api_secret=api_secret
)

access_token = data["access_token"]

with open("access_token.txt", "w") as f:
    f.write(access_token)

print("\nAccess token saved successfully.")