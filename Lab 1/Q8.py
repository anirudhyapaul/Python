# 8. WAP to check whether a number is a palindrome or not

def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")