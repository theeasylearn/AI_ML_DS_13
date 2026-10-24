# convert decimal number into binary
def binary(num):
    if num>0:
        reminder = num % 2 #1 
        num = num // 2 #32
        binary(num)
        print(reminder,end=' ')
num = 37
binary(num)


