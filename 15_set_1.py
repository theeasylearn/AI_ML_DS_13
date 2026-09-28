fruits = {'apple','banana','mango','apple','kiwi'}
print(fruits)
fruits.add('water melon')
fruits.add('graps')
fruits.add('cherry')
fruits.add('cherry') #ignore duplicate fruit
print(fruits)
fruits.remove('mango')
print(fruits)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1,set2)

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

difference = set1.difference(set2)
print(difference)

countries = ["India", "USA", "Canada", "UK", "Australia", "Germany", "India", "France", "Japan", "Brazil", "USA", "China", "Canada", "India", "Italy", "Germany", "Japan", "Australia", "India", "France"]

print(countries)
#remove duplicate value 

unique_countries = set(countries)
print(unique_countries)

#convert it into list 
countries = list(unique_countries)
countries.sort()
print(countries)