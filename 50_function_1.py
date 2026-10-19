# example of user defined function
# def function-name(parameter/input):
#   line 1
#   line 2
#   return variable/None
#function create/define
#with return value with argument
def getInterest(amount,rate,year):
    print("getInterest function executed")
    #local variable (variable created inside function. it is available only inside function)
    interest = (amount * rate * year)  / 100
    return interest #function return/throw value

#without return without argument
def printLine():
    print("-"*110)
    return None #throws nothing 

#execute/run/call function
result = getInterest(10000,10,3)
printLine()
print("Simple interest is",result)
printLine()


result = getInterest(25000,12,7)
print("Simple interest is",result)
printLine()


amount = int(input("Enter amount"))
rate = float(input("Enter rate"))
year = int(input("Enter year"))
printLine()

result = getInterest(amount,rate,year)
print("Simple interest is",result)
