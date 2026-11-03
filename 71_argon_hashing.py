from argon2 import PasswordHasher # type: ignore

original_password = "123456"
#create object
ph = PasswordHasher()

hashed_password = ph.hash(original_password)
print(hashed_password)

user_given_password = input("Enter your login password")


if ph.verify(hashed_password,user_given_password) == True:
    print("password matched successfully")
else:
    print("Password do not match")
