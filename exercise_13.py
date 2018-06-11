from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("-"*40, "Study Drill", "-"*40)
string = input('Anything else you want to declare? ')
print(f"So you said {string}.")