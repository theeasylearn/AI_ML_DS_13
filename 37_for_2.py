#example of for loop on tuple 
#findout sum and average of all values in tuple
tuple = (10,15,20,7,45,90,11,125)
sum = 0
for item in tuple:
    print(item,end=' ')
    sum = sum + item

average = sum / len(tuple)
print(f"Sum = {sum} average = ",round(average,2))

#findout and deviation 
#findout and variance