from sys import argv

# Get file name from argument passed while running the file
script, filename = argv

# Print the file name
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

input("?")

print("Opening the file...")
# Open the file with "Write" permission
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# Delete all the content of the file
target.truncate()

print("Now I'm going to ask you for three lines.")

# Get custom input from the user
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

# Write the input came from user into the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# Close the file
target.close()