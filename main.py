from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("KITE_API_KEY")

kite = KiteConnect(api_key=api_key)

with open("access_token.txt", "r") as f:
    access_token = f.read().strip()

kite.set_access_token(access_token)

# PROFILE
print("\nPROFILE\n")
print(kite.profile())

# MARGINS
print("\nMARGINS\n")
print(kite.margins())

# HOLDINGS
print("\nHOLDINGS\n")
print(kite.holdings())

# POSITIONS
print("\nPOSITIONS\n")
print(kite.positions())

# ORDERS
print("\nORDERS\n")
print(kite.orders())