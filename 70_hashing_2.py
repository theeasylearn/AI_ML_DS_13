import hashlib

name = "the easylearn academy"

result = hashlib.sha256(name.encode())
print("Hexadecimal value ",result.hexdigest()," length ",len(result.hexdigest()))


result = hashlib.sha384(name.encode())
print("Hexadecimal value ",result.hexdigest()," length ",len(result.hexdigest()))

result = hashlib.sha512(name.encode())
print("Hexadecimal value ",result.hexdigest()," length ",len(result.hexdigest()))

