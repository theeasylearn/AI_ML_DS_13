#Arbitrary Argument functions
#create function that return sum of all the values 
def getSum(*numbers): # * means numbers is tuple (read only list)
    sum = 0
    for num in numbers:
        print(num,end=' ')
        sum = sum + num 
    print("")
    return sum #this indicate function is finished 


sum = getSum(10,20,30)
print(f"sum of values = {sum}")
sum = getSum()
print(f"sum of values = {sum}")
sum = getSum(10,20,30,100)
print(f"sum of values = {sum}")
sum = getSum(10,20,30,100,500,1000)
print(f"sum of values = {sum}")
sum = getSum(10,20,30,100,500,1000,25000)
print(f"sum of values = {sum}")
