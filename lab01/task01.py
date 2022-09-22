import argparse

operands = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

parser = argparse.ArgumentParser()
parser.add_argument("num1", type=float)
parser.add_argument("operator", type=str)
parser.add_argument("num2", type=float)

args = parser.parse_args()
operation = operands.get(args.operator)
print(operation(args.num1, args.num2)) if operation else print("The operator is not valid")