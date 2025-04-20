import Scalping_functions as SC
import yfinance as yf

# terminal func to run while in clamshell, ensure amphetaime is on

# macair
# caffeinate -i python3 "{filepath}"

# macmini
# caffeinate -i python3 "{filepath}"

x = SC.Scalping_tradingfunc('QQQ') # automatically returns plot to see performance against underlying

print()
print(x[0]) # dataframe includes time series data for strategy, buy/hold asset value, and algorithm actions
print(x[1]) # trading stats (alpha and beta are benchmarked to the underlying, not the market)
