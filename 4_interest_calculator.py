# write a program to calculate and display simple interest of given amount, rate, year 
amount = float(input("Enter amount"))
rate = float(input("Enter rate"))
year = float(input("Enter year"))

#process 
interest = (amount * rate * year) / 100
#use round function to round interest
interest = round(interest,2) #round of the interest upto 2 digit after point
print(f"Simple Interest = {interest}")
