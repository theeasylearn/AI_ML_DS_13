# function that Without return value with argument 
def printLetter(letter,times):
    print(letter*times)
    return None

# function that With return value without argument 
def getPi():
    #local variable 
    pi = 22/7 
    return pi #throwing value of pi

#function execute/run/call
printLetter('@',100)
print("the easylearn academy")
printLetter('~',90)
print("Bhavnagar")
printLetter('-',80)

pi = getPi()
print("value of pi",round(pi,2))