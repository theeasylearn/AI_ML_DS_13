# write a program to count symbols
name = input("Enter your name")
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']
count = 0
for letter in name:
    if letter in symbols:
        count = count + 1
print(f"No of symbols = {count}")