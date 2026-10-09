#write a program to findout whether given number is prime number or not 
number = int(input("Enter number")) 
deviser = 2
if number%2==0:
    print("it is not prime number")
else:
    half = number // 2
    while deviser<=half: 
        reminder = number % deviser #7%2
        if reminder==0:
            print("it is not prime number")
            break #break stop loop 
        deviser = deviser + 1 #3
if deviser > half:
    print("it is prime number")
