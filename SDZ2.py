# import MetaTrader5 as mt5
import time

# mt5.initialize()

symbol = 'XAUUSD'

count = 0

def isDemandZone():
    return count % 2 == 0

def isSupplyZone():
    return count % 2 == 1

def buy():
    print('Buy Action')

def sell():
    print('Sell Action')

while (True):
    time.sleep(0.5)
    count = count + 1
    if isDemandZone():
        buy()
    elif isSupplyZone():
        sell()
    # print(mt5.symbol_info_tick(symbol).last)