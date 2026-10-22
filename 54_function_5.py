#Arbitrary Argument functions
#create function that return sum of all the values 
def getSumAverage(*numbers): # * means numbers is tuple (read only list)
    sum = 0
    for num in numbers:
        print(num,end=' ')
        sum = sum + num 
    print("")
    average = sum / len(numbers)
    return sum,average #this indicate function is finished 


result = getSumAverage(10,20,30)
print(f"sum & average of values = {result}")
result = getSumAverage(10,20,30,100)
print(f"sum & average of values = {result}")
result = getSumAverage(10,20,30,100,500,1000)
print(f"sum & average of values = {result}")
result = getSumAverage(10,20,30,100,500,1000,25000)
print(f"sum & average of values = {result}")
