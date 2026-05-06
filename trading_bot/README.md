# Trading Bot CLI

## How to run

### Market Order:
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order:
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 30000

## Features
- CLI-based order input
- Market and Limit order support
- Input validation
- Logging system