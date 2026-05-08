import yfinance as yf
import time

# -------- CONFIG --------
lot_size = 50   # Nifty lot size

# Your trade (EDIT if needed)
positions = {
    "CE_SELL": {"strike": 24600, "sell_price": 80},
    "CE_BUY":  {"strike": 25000, "buy_price": 25},
    "PE_SELL": {"strike": 23700, "sell_price": 85},
    "PE_BUY":  {"strike": 23300, "buy_price": 20}
}

# -------- FUNCTIONS --------

def get_nifty_price():
    nifty = yf.Ticker("^NSEI")
    data = nifty.history(period="1d", interval="1m")
    return round(data["Close"].iloc[-1], 2)

def get_ltp_input():
    print("\nEnter current option prices:")
    ce_sell = float(input("24600 CE current price: "))
    ce_buy  = float(input("25000 CE current price: "))
    pe_sell = float(input("23700 PE current price: "))
    pe_buy  = float(input("23300 PE current price: "))
    return ce_sell, ce_buy, pe_sell, pe_buy

def calculate_pnl(ce_s, ce_b, pe_s, pe_b):
    pnl = 0
    
    pnl += (positions["CE_SELL"]["sell_price"] - ce_s) * lot_size
    pnl += (pe_s - positions["PE_SELL"]["sell_price"]) * -lot_size  # corrected logic
    
    pnl += (ce_b - positions["CE_BUY"]["buy_price"]) * lot_size
    pnl += (pe_b - positions["PE_BUY"]["buy_price"]) * lot_size
    
    return pnl

def adjustment_signal(nifty_price):
    if nifty_price > 24400:
        return "⚠️ Shift CALL side UP"
    elif nifty_price < 23900:
        return "⚠️ Shift PUT side DOWN"
    else:
        return "✅ Within range"

# -------- MAIN LOOP --------

while True:
    try:
        nifty_price = get_nifty_price()
        print(f"\n📈 NIFTY: {nifty_price}")

        ce_s, ce_b, pe_s, pe_b = get_ltp_input()

        pnl = calculate_pnl(ce_s, ce_b, pe_s, pe_b)
        signal = adjustment_signal(nifty_price)

        print(f"\n💰 LIVE P&L: ₹{round(pnl,2)}")
        print(f"📊 STATUS: {signal}")

        if pnl < -20000:
            print("🚨 STOP LOSS HIT - EXIT ALL")

        print("\nRefreshing in 60 sec...\n")
        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        break