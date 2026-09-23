fruits = ['apple','mango','banana','kiwi','orange']
print(fruits)
#append at last 
fruits.append('water melon')
fruits.append('graps')

fruits.insert(0,'pineapple') #insert at 1st position
fruits.insert(2,'sweet lime') #insert after apple
print(fruits)
vegis = ['potato','cucumber','tomato']
fruits.extend(vegis)
print(fruits)
print(vegis)
vegis.remove('potato')
vegis.pop(1) # tomato
print(vegis)
vegis.clear() #remove all item 
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
# fruits_2 = fruits #store reference of list into list_2 (do not copy list)
fruits_2 = fruits.copy()
print(fruits,fruits_2)
fruits_2.clear()
print(fruits,fruits_2)