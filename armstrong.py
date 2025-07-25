def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

def print_armstrong_in_range(start, end):
    print(f"Armstrong numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number)

"""example range """
start_range = 1
end_range = 101
print_armstrong_in_range(start_range, end_range)