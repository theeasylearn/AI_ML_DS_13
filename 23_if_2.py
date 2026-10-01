# write a program to findout whether given shape is portrait or landscape or square from user given length and width.
#task findout display ratio of width vs length
length = int(input("Enter length"))
width = int(input("Enter width"))

if length>width:
    print("shape is portrait")
if width>length:
    print("shape is landscape")
if width==length:
    print("shape is square")

print("Good bye")