import MetaTrader5 as mt5
import time

mt5.initialize()

symbol = 'XAUUSD'

while(True):
    time.sleep(0.5)
    print(mt5.symbol_info_tick(symbol).last)