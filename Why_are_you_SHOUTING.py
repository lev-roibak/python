"""
Create a small program that asks the user to enter something he likes to eat using input().
After the user enters the food the program prints prints Yummy! -
unless the entered word was all uppercase -
in this case it prints OK BUT WHY ARE YOU SHOUTING? instead.
"""

s = input('Enter something you like to eat:\n')

if s.isupper():
    print("OK BUT WHY ARE YOU SHOUTING?")
else:
    print("Yummy!")
