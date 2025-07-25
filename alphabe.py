def print_x_with_alphabets(n):
    if n % 2 == 0:
        print("Please enter an odd number for proper symmetry.")
        return

    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print("*", end="")
            elif j > i and j < n - i - 1:
                # Letter between the diagonals
                letter_index = j - i - 1
                print(chr(65 + letter_index % 26), end="")
            elif j < i and j > n - i - 1:
                # Mirror the above logic
                letter_index = i - j - 1
                print(chr(65 + letter_index % 26), end="")
            else:
                print(" ", end="")
        print()

# Example usage
rows = 7
print_x_with_alphabets(rows)