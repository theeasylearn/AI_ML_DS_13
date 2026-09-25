book = {} #empty 
print(book)
#adding new key value pair
book['name'] = 'The Atomic Habit'
book['price'] = 500
book['author'] = "James clear"

print(book)

#add tuple into dictionary
book['chapter'] = (1,2,3,4,5)
#add list into dictionary
book['topics'] = ['index','introduction','habits','summery']

print(book)

# book['chapter'][0] = 10 #TypeError: 'tuple' object does not support item assignment
book['topics'][0] = 'beginning'

del book['chapter']
book['name'] = "the power of habits"
print(book)