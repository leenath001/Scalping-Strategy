# Scalping-Strategy
Functions for executing scalping strategy. Yfin API will rate-limit users if too many calls, may have to run alone without other strategies calling API.

Goal : Strategy aims to profit from 'up' moves while staying on the sideline for down moves. Algorithm constantly receives quotes to identify movements within short time-frames. 
*  To run tradingfuncs, create an interactive brokers account and download IB Gateway (API must be simultaneously running alongside the function inside a terminal). 
*  To run autonomously, download 'Amphetamine' (mac) on app store. Also, employ caffeinate -i python3 '{filepath of execution files}' to run within terminal. Processes will run in the background while laptop/computer is inactive/closed. Trading functions run until Ctrl + C is used.

## Scalping_funcs.Scalping_tradingfunc(ticker) (to be tested next market session)
*  function for employing scalping strategy using IB gateway.
*  Strategy continuously pings yfin API to grab ticker quotes and determines if current is > last. Strategy aims to profit on uptrends, while staying on the sideline for downtrends.
*  Buy condition: Buy if most recent quote (x) is greater than one before (x-1). Hold for all other instances following.
*  Sell conditon: Sell if most recent quote (x) is less than one before (x-1). Do nothing for all other instances following.
*  To change time between quotes, see lines 111 and 138. 
