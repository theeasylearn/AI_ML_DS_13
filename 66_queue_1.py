# concept queue
queue =  [] 
front = - 1
rear = - 1
size = 5
#enqueue function is used to insert new value at the end of queue (rear end)
def enqueue(item):
    global queue,front,rear,size
    if front == -1:
        front = 0 
    if rear<size-1:
        rear = rear + 1
        queue.append(item)
    else:
        print("Queue Overflow")
def display():
    global queue,front,rear
    if front == -1:
        print("queue is empty")
    else:
        for index in range(front,rear+1):
            print(queue[index],end=' ')
        print("")
def dequeue():
    global queue,front,rear,size
    print(f"front = {front} rear = {rear}")
    if front == -1 or front > rear:
        print("queue underflow")
    else:
        queue[front] = None 
        front = front + 1 
while True:
    print("Press 1 for Enqueue(insert new item at rear end) operation")
    print("Press 2 for Dequeue(delete existing item from front end) operation")
    print("Press 3 for Display operation")
    print("Press 0 for exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        value = input("Enter value")
        enqueue(value)
    elif choice == 2:
        dequeue() # 10
    elif choice == 3:    
        display()
    elif choice == 0:
        print("Good bye")
        break
    else:
        print("invalid choice")
