def count_characters(s):
    vowels = "aeiouAEIOU"
    digits = "0123456789"

    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    symbol_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Symbols:", symbol_count)

# Example usage:
input_string = input("Enter a string: ")
count_characters(input_string)