# crypto-funding-rate-monitor
A small tool that checks the funding rate of all Binance USDT futures. It automatically finds every valid symbol, gets the current funding rate, and alerts you when the number becomes extremely positive or extremely negative

# Background Knowledge
Funding rate is a small fee that shows which side has too many people betting the same way with leverage. Very positive means lots of people are betting up and must pay the people betting down; very negative means lots are betting down and must pay the people betting up. When the number gets extreme, it usually means the crowd is overloaded and the market often makes a big move because those traders get liquidated. It’s a useful warning, but not something to rely on alone.<br><br>
Normal is around 0.00% to 0.01%. If it goes very positive (like +0.05% or higher), too many people are betting up and must pay people betting down. If it goes very negative (like –0.05% or lower), too many people are betting down and must pay people betting up. When it becomes extreme like this, it usually means the market is overloaded on one side and a big move can happen, so it’s a warning sign but not a perfect prediction. The only smart action is to avoid leverage and either use small spot or simply wait.

# Features
- Fetches all Binance Futures symbols that end with `USDT`
- Gets the latest funding rate via the Binance API
- Classifies each symbol as `VERY HIGH`, `VERY LOW`, or `OK`
- Background Python thread updates data every 60 minutes
- Frontend auto-refreshes the table every second

# Instructions
## Download the following <br>
`pip install flask requests`<br><br>

## Run
`python funding_rate_monitor.py` <br><br>
Open `http://127.0.0.1:5000` in the browser

