import streamlit as st

st.set_page_config(page_title="NIFTY Options Strategy", layout="centered")

st.title("📊 NIFTY Iron Condor Builder")

# User Inputs
spot = st.number_input("Enter NIFTY Spot Price", value=24100, step=50)
capital = st.number_input("Capital (₹)", value=1000000)

st.markdown("---")

# Strategy Parameters
distance = st.slider("Strike Distance (points)", 200, 500, 300)
hedge_width = st.slider("Hedge Width (points)", 200, 500, 300)

# Calculate Strikes
put_sell = int(spot - distance)
put_buy = int(put_sell - hedge_width)

call_sell = int(spot + distance)
call_buy = int(call_sell + hedge_width)

st.subheader("📌 Suggested Iron Condor")

col1, col2 = st.columns(2)

with col1:
    st.write("🟢 SELL PUT:", put_sell)
    st.write("🔴 BUY PUT:", put_buy)

with col2:
    st.write("🟢 SELL CALL:", call_sell)
    st.write("🔴 BUY CALL:", call_buy)

# Range
st.markdown("---")
st.subheader("📈 Profit Range")
st.success(f"{put_sell}  ➝  {call_sell}")

# Lot Calculation
margin_per_lot = 180000  # approx
lots = int(capital // margin_per_lot)

st.subheader("💰 Position Sizing")
st.write(f"Recommended Lots: {lots}")
st.write(f"Margin Used: ₹{lots * margin_per_lot:,}")

# Risk Estimation
max_loss_per_lot = hedge_width * 50  # rough estimate
total_risk = max_loss_per_lot * lots

st.subheader("⚠️ Risk Estimate")
st.error(f"Max Risk (approx): ₹{total_risk:,}")

# Stop Loss Levels
st.subheader("🚨 Exit Levels")
st.write(f"Upper SL: {call_sell + 50}")
st.write(f"Lower SL: {put_sell - 50}")

st.markdown("---")
st.caption("⚠️ Educational tool. Always verify with live option chain.")
