import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", type=str)
    args = parser.parse_args()

    result = proccessing(args.expression)
    print(result)


def proccessing(expression: str):
    symbols = "0123456789+-"
    for index, char in enumerate(expression):
        if (char not in symbols) or ((char == "+" or char == "-") and (expression[index - 1] == char)):
            return (False, None)
    return (True, eval(expression))


if __name__ == "__main__":
    main()
