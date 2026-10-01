#write a program to findout profit or loss amount from given purchase and sales price of product
#task 
# also calculate and display profit or loss percentage 
#decide input 
purchase_price = int(input("Enter purchase price"))
sales_price = int(input("Enter sales price"))

#find difference 
difference = sales_price - purchase_price
if difference>0: #< <= > >= != ==
    print(difference, " is your profit")

if difference<0: #< <= > >= != ==
    print(difference, " is your loss")

print("Good bye")