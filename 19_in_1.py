#example of in operator 

numbers = [10,20,30,40,50,60,70,80,90,100]

value = 550
isFound = value in numbers
print(f"is {value} found ",isFound)

isFound = value not in numbers
print(f"is {value} not found ",isFound)
