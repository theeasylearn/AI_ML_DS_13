# example of circular queue 
list = []
front = -1
rear = -1
size = 5

def enqueue(value):
    global list,front,rear,size 
    if front == -1:
        front=0
    if rear < size - 1 or rear < front: # 5 -1 =4
        rear = rear + 1 #0
        list.append(value)
        print("value has been added into circular queue")
    elif front>1:
        rear = 0
        list.append(value)
        print("value has been added into circular queue") 
    else:    
        print("Circular queue overflow")

def dequeue():
    global list,front,rear,size
    print(f"front = {front} rear = {rear}")
    if front == -1 or front > rear:
        print("circular queue underflow")
    else:
        list[front] = None 
        front = front + 1 
def display():
    global list,front,rear
    if front == -1:
        print("queue is empty")
    else:
        print("-"*100)
        for index in range(front,rear+1):
            print(list[index],end=' ')
        print("")
        print("-"*100)

while True:
    print("Press 1 for Enqueue(insert new item at rear end) operation")
    print("Press 2 for Dequeue(delete existing item from front end) operation")
    print("Press 3 for Display operation")
    print("Press 0 for exit")
    choice = int(input("Enter your choice"))
    match choice:
        case 1: # choice == 1
            value = input("Enter value to insert in circular queue")
            enqueue(value)
        case 2: # choice == 2
            dequeue()
        case 3: 
            display()
        case 0:
            print("good bye")
            break 
        case _: # all cases are false 
            print("Invalid choice")
