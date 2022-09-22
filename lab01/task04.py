import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-W", type=int)
    parser.add_argument("-w", nargs='+', type=int)
    parser.add_argument("-n", type=int)
    args = parser.parse_args()

    if len(args.w) != args.n:
        print("The amount of items you've entered does not match the actual one")
        return

    print(maxweight(args.W, args.w))


def maxweight(W, w):
    w = [0] + w
    items = len(w)
    capacity = W + 1
    matrix = [[0 for i in range(items)] for i in range(capacity)]

    for i in range(1, items):
        for j in range(1, capacity):
            matrix[j][i] = matrix[j][i - 1]
            if w[i] <= j:
                val = matrix[j - w[i]][i - 1] + w[i]
                if matrix[j][i] < val:
                    matrix[j][i] = val
    return matrix[-1][-1]


if __name__ == "__main__":
    main()
