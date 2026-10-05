# write a program to findout & whether given year is leap year or not
year = int(input("Enter year")) #2028
reminder1 = year % 4 #0
reminder2 = year % 100 #28
reminder3 = year % 400 # 28
if reminder1 == 0 and reminder2!=0:
    print("this is leap year")
else:
    if reminder2 == 0 and reminder3 == 0:
        print("this is leap year")
    else:
        print("this is not leap year")
