from kiteconnect import KiteConnect
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("KITE_API_KEY")

# Initialize Kite
kite = KiteConnect(api_key=api_key)

# Read saved access token
with open("access_token.txt", "r") as f:
    access_token = f.read().strip()

kite.set_access_token(access_token)

try:
    # Fetch holdings
    holdings = kite.holdings()

    # Convert to DataFrame
    df = pd.DataFrame(holdings)

    # Save to CSV
    df.to_csv("holdings.csv", index=False)

    print("\nHoldings exported successfully.")
    print("File saved as holdings.csv")

except Exception as e:
    print("\nError:")
    print(e)