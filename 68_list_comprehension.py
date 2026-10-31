numbers = [1, 2, 3, 4, 5,10]

# squares = []
# for num in numbers:
#     squares.append(num ** 2)

#list comprehension 
squares = [num ** 2 for num in numbers]
print(squares)

#create list and store 5 none
list = [None for i in range(0,5)]
print(list)