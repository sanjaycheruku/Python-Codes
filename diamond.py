rows = int(input("Enter the number of rows: "))

# Upper half
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
