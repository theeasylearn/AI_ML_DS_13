center = {'name':'the easylearn academy','year':2013,'city':'Bhavnagar','pincode':364001}

print(center)
center_2 = center.copy()
print(center_2)
center_2.clear() #remove all key value pair keep dictionary
print(center_2)
del center_2 #delete dictionary itself
print("keys ", center.keys())
print("values ", center.values())
print("Dictionary as item ",center.items())
print("institute name ",center.get("name","not found"))
# print(center['email'])
print("institute email address ",center.get("email","not found"))
center.pop('pincode')
print(center)
center.popitem()
print(center)
center.update({'owner':'Ankit Patel','year':2012})
print(center)

#create list
student = ['name','age','gender','email','dob']
print(student)

#create dictionary using list 
dishant = dict.fromkeys(student)
harshali = dict.fromkeys(student)
kartik = dict.fromkeys(student)

print(dishant,kartik,harshali)

dishant['name'] = 'Dishant Vithani'
dishant['age'] = 21
dishant['gender'] = 'Male'
print(dishant)