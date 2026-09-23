line = "the easylearn academy"
city = " bhavnagar"
pincode = 364001 #integer 
print(line)
print(line[0]) #t
print(line[0:2]) #th
print(line[0:3]) #the
print(line[3:]) #easylearn academy
print(line[:3]) #the
print(line[::2]) #skip every 1 letter after 1 letter 
print(line[::-1]) #print variable in reverse order 
print(line * 3)
print(line + city)
# print(line + pincode) #error because you can't use + with string and integer value
print(line + str(pincode)) 
print(line,pincode)
line = 'T.E.A'
print(line)
# line[0] = 'X' you can not change part of string because string is immutable
