def getMerit(maths,science,english,gujarati,hindi,social):
    print(f"maths = {maths},science = {science} ,english = {english},gujarati = {gujarati},hindi = {hindi},social = {social}")
    total = maths + science + english
    return total

m = int(input("Enter Maths marks: "))
s = int(input("Enter Science marks: "))
e = int(input("Enter English marks: "))
g = int(input("Enter Gujarati marks: "))
h = int(input("Enter Hindi marks: "))
sc = int(input("Enter Social Science marks: "))

# wrong way of calling function
total = getMerit(g,h,sc,m,s,e)
print("Total ",total)

#keyword arguments
total = getMerit(gujarati=g,hindi=h,social=sc,maths=m,science=s,english=e)
print("Total ",total)
