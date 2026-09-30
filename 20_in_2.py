#example of in operator 

fruits = ('apple','banana','mango','apple','kiwi')

# value = 'mango'
value = input("What is your favourite fruit?")
isFound = value in fruits
print(f"is {value} found ",isFound)

isFound = value not in fruits
print(f"is {value} not found ",isFound)
