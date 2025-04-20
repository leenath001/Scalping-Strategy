import Scalping_functions as SC
import yfinance as yf

# terminal func to run while in clamshell, ensure amphetaime is on

# macair
# caffeinate -i python3 "/Users/leenath/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Code/Algos/Scapling_execution.py"

# macmini
# caffeinate -i python3 "/Users/leenath/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Code/Algos/Scapling_execution.py"

# Other strats : continual put, pair trading, arbitrage? 

x = SC.Scalping_tradingfunc('QQQ')
print()
print(x[0])
print(x[1])