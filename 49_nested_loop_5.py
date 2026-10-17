# write a program to findout whether given number is armstrong number or not 
# input : 153 
# process  : 1x1x1 5x5x5 3x3x3 -> 1 + 125 + 27 = 153 (armstrong number)
# input : 1634 
# process : 1x1x1x1 6x6x6x6 3x3x3x3 4x4x4x4 = 1 + 1296 + 81 +256 = 1634 (armstrong number)
# input : 257
# process : 2x2x2 5x5x5 7x7x7 -> 8 + 125 + 343 = 476 (not armstrong )

num = int(input("Enter number ")) #how many digits this num variable has (legnth)
length = len(str(num))
original_num = num 
total = 0
while num>0: #outer loop
    power = 1
    reminder = num % 10 #3
    for i in range(0,length): #inner loop 
        power = power * reminder 
    total = total + power 
    num = num // 10 #15.3

if total==original_num:
    print("armstrong number")
else:
    print("not an armstrong number")



