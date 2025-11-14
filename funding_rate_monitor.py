import requests
import time

def get_all_symbols():
    all_assets_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"  #Binance API
    data = requests.get(all_assets_url).json()  #Convert to json so that can be the handleable object in Python

    symbols = []
    for item in data["symbols"]:  # When you do data["symbols"], you're accessing the key called "symbols" in that dictionary
        symbol = item["symbol"]  # A dictionary as well

        #If the coin is a normal USDT pair and it does not have an underline, add it to the list
        if symbol.endswith("USDT") and "_" not in symbol:  #Only keeps coins that are USDT futures pairs, reject underline because symbols with that are dated contracts which are not funding rate
            symbols.append(symbol) 
    return symbols

def get_funding_rate(symbol):
    url = f"https://fapi.binance.com/fapi/v1/premiumIndex?symbol={symbol}"
    visit_the_url = requests.get(url).json()
    return float(visit_the_url["lastFundingRate"]) * 100 #The fundind rate will be in % form 

def monitor_all_symbols():
    symbols = get_all_symbols()
    print(f"Monitoring {len(symbols)} symbols... \n")

    ceilling = 0.05
    floor = -0.05

    while True:
        print("--- Checking Funding Rates ---")
        for symbol in symbols:
            try:
                rate = get_funding_rate(symbol)
            except Exception: # without Exception the except catches everything so you can't interrupt the program by doing control C
                continue

            if rate > ceilling:
                print (f"ALERT: {symbol} VERY HIGH: {rate:.4f}%")
            elif rate < floor:
                print(f"ALERT: {symbol} VERY LOW: {rate:.4f}%")
            else:
                print(f"OK: {symbol} {rate:.4f}%")

        time.sleep(3600) #check every hour

if __name__ == "__main__":
    monitor_all_symbols()