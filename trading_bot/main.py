import argparse
from orders import place_order
from validators import validate_order
from logger import log_error

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_order(args.type, args.price)

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("Order Successful!")
    print(order)

except Exception as e:
    print("Error:", e)
    log_error(str(e))