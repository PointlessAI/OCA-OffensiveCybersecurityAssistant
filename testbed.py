# Testing scratchpad
# Code not implented - for testing only
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-g", nargs='?', help="General Assistant", type=int, default=0)
parser.add_argument("-t", nargs='?', help="Terminal Assistant", type=int, default=0)
parser.add_argument("-c", nargs='?', help="Code Generator", type=int, default=0)

args = parser.parse_args()

if args.g is not None:
    print({args})
    print(f"Value of -g: {args.g}")
else:
    print("No value provided for -g")
    print(f"Default value of -g: {args.g}")