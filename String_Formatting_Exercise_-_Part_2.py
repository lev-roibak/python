"""
Use the code from the previous exercise and input(), to write a short program that asks the user the following questions:

What is the name of the father?
How many sons he has?
How many daughters he has?

And prints out the answer.
"""
name = input('What is the name of the father? ')
print(name)
sons = input('How many sons he has? ')
print(sons)
daughters = input('How many daughters he has? ')
print(daughters)
print(f"{name.capitalize()} has {sons + daughters} kids.")
