"""
The wanted result:
I am shouting your words:
GOOD MORNING WORLD
Your words as a title:
Good Morning World
Your words as an inverse title:
gOOD mORNING wORLD

"""

s = input('Please enter a sentence:\n')

print("I am shouting your words:")
print(s.upper())

print("Your words as a title:")
result = ' '.join(elem.capitalize() for elem in s.split())
print(result)

print("Your words as an inverse title:")
s2 = s.upper()
res = ' '.join(element[0].lower() + element[1::] for element in s2.split())

print(res)
