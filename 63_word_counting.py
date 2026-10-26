# write a program to count no of words (space)
name = input("Enter your name")
space = 1
for letter in name:
    # print(letter)
    if letter == ' ':
        space = space + 1

print(f"No of words in {name} = {space}")