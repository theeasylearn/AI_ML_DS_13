#write a program to calculate compound interest of given amount, rate, year
amount = int(input("Enter amount"))
rate = float(input("Enter rate"))
year = int(input("Enter year")) #5
total_interest = 0

while year>=1:
    interest = (amount * rate) / 100
    total_interest = total_interest + interest 
    amount = amount + interest
    year = year - 1
print("total compound interest",round(total_interest,2))