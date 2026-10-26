# write a program to convert decimal number into hexadecimal number system 
def hexadecimal(number):
    if number>0:
        reminder = number % 16
        number = number // 16
        if reminder == 10:
            reminder = 'A'
        elif reminder == 11:
            reminder = 'B'
        elif reminder == 12:
            reminder = 'C'
        elif reminder == 13:
            reminder = 'D'
        elif reminder == 14:
            reminder = 'E'
        elif reminder == 15:
            reminder = 'f'
        hexadecimal(number)
        print(reminder,end='')

number = int(input("Enter number"))
hexadecimal(number)