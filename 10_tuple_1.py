#example of tuple 
tuple = ('Ankit',"Patel",True,False,41,3.14)
city = ("Bhavnagar",364001)
print(tuple) 
print(city) 
print(tuple[0]) #Ankit
print(tuple[0:2]) #Ankit Patel
print(tuple[2:]) #True,False,41,3.14
print(tuple[:3]) #'Ankit',"Patel",True
print(city * 3) # "Bhavnagar",364001 "Bhavnagar",364001 "Bhavnagar",364001
print(tuple + city)

#you trying to change value in tuple at 0th position
# tuple[0] = "Dishant" #error because tuple is immutable 

#you are trying to delete value which is not possible 
# del tuple[0] 
print("Good bye")
