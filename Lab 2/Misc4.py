# 4. Write a program to find LCM of two Numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")
