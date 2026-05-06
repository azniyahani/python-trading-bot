# Trading Bot CLI

## Overview
This is a simple Python-based trading bot project built for learning purposes.  
It simulates placing market and limit orders using command-line inputs.  
(No real API keys are used.)

## Features
- CLI-based order input
- Market order support
- Limit order support
- Input validation
- Logging system

## How to Run

### Market Order
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 30000
