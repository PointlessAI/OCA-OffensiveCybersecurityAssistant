# Testing scratchpad
# Code not implented - for testing only
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-g", nargs='?', help="General Assistant", type=int, default=1)
parser.add_argument("-t", nargs='?', help="Terminal Assistant", type=int, default=1)
parser.add_argument("-c", nargs='?', help="Code Generator", type=int, default=1)

args = parser.parse_args()


print(f"Value of -g: {args.g}")
print(f"Value of -t: {args.t}")
print(f"Value of -c: {args.c}")