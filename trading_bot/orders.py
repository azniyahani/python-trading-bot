from logger import log_info

def place_order(symbol, side, order_type, quantity, price=None):
    order = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "price": price,
        "status": "SUCCESS"
    }

    log_info(f"Order placed: {order}")
    return order