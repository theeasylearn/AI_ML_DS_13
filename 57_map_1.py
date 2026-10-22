numbers = [1,2,3,4,5]
print(numbers)

#generate square 
# squared = [] 
# for num in numbers:
#     squared.append(num * num)
squared = map(lambda num : num * num,numbers)
print(list(squared))

decision = ['Yes','No','Yes','No','yes']

result = map(lambda item: 1 if item == 'Yes' else 0, decision)
print(list(result))
