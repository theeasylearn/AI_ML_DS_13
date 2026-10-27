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
    if front == -1 or front >= rear:
        print("queue underflow")
    else:
        queue[front] = None 
        front = front + 1 
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
enqueue(60)
display()
dequeue() # 10
dequeue() # 20
dequeue() # 30
display() # 40 50
dequeue() # 40
dequeue() # 50