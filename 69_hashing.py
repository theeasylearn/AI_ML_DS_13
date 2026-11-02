#hashing 

name = "the easylearn academy"
address = "105, eva surbhi, opp aksharwadi temple, waghawadi road, bhavnagar"

print(f"Name = {name} length = ",len(name))
print(f"address = {address} length = ",len(address))

#hash 

name_hash = hash(name)
address_hash = hash(address)

print(f"name hash = {name_hash} length = ",len(str(name_hash)))
print(f"address hash = {address_hash} length = ",len(str(address_hash)))

