"""
Write a short program that uses the following pieces of information:

    The name of a man,
    The number of sons he has
    The number of daughters he has

And prints out his name (capitalized) and his total number of kids :
"""

name = "joe"
sons = 2
daughters = 3

# ----- ENTER YOUR CODE HERE --------
s = f"{name.capitalize()} has {sons + daughters} kids."
# -----------------------------------

print(s)
assert s == "Joe has 5 kids."
print("OK")
