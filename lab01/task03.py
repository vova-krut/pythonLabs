import argparse

parser = argparse.ArgumentParser()
parser.add_argument("expression", type=str)
args = parser.parse_args()

symbols = "0123456789+-"

for index, char in enumerate(args.expression):
    if (char not in symbols) or ((char == "+" or char == "-") and (args.expression[index - 1] == char)):
        result = (False, None)
        print(result)
        exit(1)

result = (True, eval(args.expression))
print(result)