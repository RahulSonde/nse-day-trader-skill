#!/usr/bin/env python3
"""Generate a local NSE F&O universe file for trader-scanner."""

NSE_FNO_SYMBOLS = [
    "^NSEI",         # Nifty 50 Index
    "RELIANCE.NS",   # Reliance Industries
    "TCS.NS",        # Tata Consultancy Services
    "HDFCBANK.NS",   # HDFC Bank
    "ICICIBANK.NS",  # ICICI Bank
    "INFY.NS",       # Infosys
    "SBIN.NS",       # State Bank of India
    "BHARTIARTL.NS", # Bharti Airtel
    "ITC.NS",        # ITC Limited
    "KOTAKBANK.NS",  # Kotak Mahindra Bank
    "LT.NS",         # Larsen & Toubro
    "AXISBANK.NS",   # Axis Bank
    "HINDUNILVR.NS", # Hindustan Unilever
    "BAJFINANCE.NS", # Bajaj Finance
    "MARUTI.NS",     # Maruti Suzuki
    "SUNPHARMA.NS",  # Sun Pharma
    "TITAN.NS",      # Titan Company
    "TATASTEEL.NS",  # Tata Steel
    "NTPC.NS",       # NTPC
    "POWERGRID.NS"   # Power Grid Corporation
]

def main():
    import os
    os.makedirs("trader", exist_ok=True)
    universe_path = "trader/universe.txt"
    with open(universe_path, "w", encoding="utf-8") as f:
        for sym in NSE_FNO_SYMBOLS:
            f.write(sym + "\n")
    print(f"Successfully wrote {len(NSE_FNO_SYMBOLS)} NSE F&O symbols to {universe_path}")

if __name__ == "__main__":
    main()