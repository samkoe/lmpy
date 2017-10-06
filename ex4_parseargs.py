# ex4.py

import argparse
import random

parser = argparse.ArgumentParser()

# Add flags
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
parser.add_argument("-i", "--icecream", help="order ala mode", action="store_true")
parser.add_argument("-ch", "--cheese", help="we'll put cheese on that", action="store_true")

# Add options
parser.add_argument("cheeseburgers", help="display the number of cheeseburgers ordered", type=int)
parser.add_argument("size", help="display the size of the order", type=str, choices=["small", "medium", "large"])
parser.add_argument("side", help="show the side order", type=str, choices=["fries", "tots", "rings"])

# Add positional arguments
parser.add_argument("echo")

# Execute correct functionality
args = parser.parse_args()

# Options functionality
print("You ordered {} cheeseburgers.".format(args.cheeseburgers))
print("The size of your meal is {}.".format(args.size))
print("Your side order is {}.".format(args.side))

# Flags functionality
if args.verbosity:
	print("verbosity turned on")
if args.cheese:
	print("we'll put cheese on that")
if args.icecream:
	print("ice cream added to your order")

# Positional args functionality
print(args.echo)