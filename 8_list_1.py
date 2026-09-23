list = ['Dishant',100,'Vithani',3.14,True,False]
list_2 = [500,'Bhavnagar']
print(list)
print(list[0]) #Dishant
print(list[0:3]) # Dishant 100 Vithani
print(list[1:3]) # 100 Vithani
print(list[2:]) # Vithani 3.14 True False
print(list * 2) 
print(list + list_2)
del list_2[0] #del keyword remove 0th index value 500
print(list_2)
#delete entire list
del list_2
# print(list_2) will return nameerror NameError