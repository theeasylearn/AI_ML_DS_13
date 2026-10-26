# concept of stack 
stack = []
size = 5
top = - 1
def push(item):
    global stack,size,top 
    if top==size-1:
        print("Stack Overflow")
    else:
        top = top + 1 
        stack.append(item)

def display():
    global stack,top 
    print("-"*100)
    for index in range(top,-1,-1):
        print(stack[index])
def pop():
    global stack,top 
    if top == -1:
        print("stack underflow")
    else:
        del stack[top]
        top = top - 1

# push(10)
# push(20)
# push(30)
# push(40)
# push(50)
# push(100)
# display()
# pop()
# pop()
# pop()
# pop()
# pop()
# pop()
# display()

while True:
    print("Press 1 to push item into stack")
    print("Press 2 display all values in stack")
    print("Press 3 to pop value from stack")
    print("Press 0 to exit")
    choice = int(input("Enter your choice "))
    if choice == 1:
        item = input("Enter item")
        push(item)
    elif choice == 2:
        display()
    elif choice == 3:
        pop()
    elif choice == 0:
        print("Exit from program")
        break 