import argparse
import operator

parser = argparse.ArgumentParser()
parser.add_argument("func", type=str)
parser.add_argument("num1", type=float)
parser.add_argument("num2", type=float)
args = parser.parse_args()

func = getattr(operator, args.func, None)

try:
    print(func(args.num1, args.num2)) if func else print("Func name is not correct")
except ZeroDivisionError:
    print("You can't divide by zero")
