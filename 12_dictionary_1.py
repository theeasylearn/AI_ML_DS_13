product = {'name':"IPhone 18 pro max","price":300000,"weight":250.25,'available':True}
print(product)
#print name key's value
print(product['name']) # IPhone 18 pro max
print(product['price']) # 300000

#update value
product['price'] = 245321
print(product['price']) # 245321
#add new key value pair
product['company'] = "Apple"
print(product['company']) # Apple

#delete key 
del product['available']
print(product)
