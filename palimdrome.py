'''  
# with using scling
text = input("Enter a string: ")


if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
'''

#without using scling
text =' mam'

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  

if text == reversed_text:
    print("It is a palindrome.")
else:
    print(text + "It is not a palindrome.")
