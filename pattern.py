def diamond(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(n - 1, -1, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()


if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    diamond(n)