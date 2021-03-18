BTC – Difference


Introduction
Trading algorithm model based on th BTC furues / BTC price difference.  The model aim to set dynamic triggers for open the positions. Based on the conditions, the algorithm open when the price difference became large. The model based with a dynamic trigger.  Opening at the same time Long position with BTC and Short position with BTC futures and close it whe the price difference became small.
________________________________________________________________________________
Exchange: Binance
Fees = 0.32%
________________________________________________________________________________
Server
The server open the positions with a VPS
________________________________________________________________________________

Trading Algorithm

if P < dynamic_OPEN:

  - OPEN positions
    • Buy X BTC
    • Sell X BTC futures


if P < dynamic_CLOSE:

   - CLOSE positions
    • Sell X BTC
    • Close X BTC futures

________________________________________________________________________________
Model parameters 
dynamic_OPEN = open_function( RSIdiff  , BTCdiff , Volatility, Volumes)   ← ??? da decidere
dynamic_CLOSE = close_function( RSIdiff  , BTCdiff , Volatility, Volumes)  ← ??? da decidere

BTCdiff = BTC furues / BTC 
RSIdiff  = 
Volatility = 
Volumes = volumes of  BTC furues and BTC 
________________________________________________________________________________
Sizing rules
