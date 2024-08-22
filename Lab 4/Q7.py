# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only. Example: If the following words is given as input to the program: 2 cats and 3 dogs. Then, the output of the program should be: ['2', '3']

input_string = input("Enter a sequence of words separated by whitespace: ")
words = input_string.split()
digit_words = [word for word in words if word.isdigit()]

print(digit_words)
