# example of for loop 
#findout maximum value and its position in list 
list = [10,15,200,7,45,90,-11,125]
max = list[0] # 10
position = 0
for index,value in enumerate(list): #20 1
    # print(value,index,end=' ')
    if max<value: #15<20
        max = value #20
        position = index # 2

print(f"Maximum value = {max} and it's position {position}")

#findout minimum value and its position 
#findout second minimum value and its position 
#findout second maximum value and its position 
