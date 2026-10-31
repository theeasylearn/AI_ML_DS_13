
# Example of Circular Queue
queue = [None, None, None, None, None]
front = -1
rear = -1
size = 5

# Enqueue: Insert new element at rear end
def enqueue(value):
    global queue, front, rear, size
    # Check overflow condition
    if (rear + 1) % size == front:
        print("Circular queue overflow")
        return #function stop 
    # If queue is empty
    if front == -1:
        front = 0
    # Increment rear circularly
    rear = (rear + 1) % size
    # Insert new value
    queue[rear] = value
    print("Value has been added into circular queue")
# Dequeue: Delete element from front end
def dequeue():
    global queue, front, rear, size
    # Check underflow condition
    if front == -1:
        print("Circular queue underflow")
        return
    # Display deleted element
    print("Deleted element:", queue[front])
    # Remove element
    queue[front] = None
    # If only one element is present
    if front == rear:
        front = -1
        rear = -1
    else:
        # Increment front circularly
        front = (front + 1) % size
    print("Element has been deleted from circular queue")

# Display: Display all elements of circular queue
def display():
    global queue, front, rear, size
    print(f"front = {front} rear = {rear}")
    if front == -1:
        print("Circular queue is empty")
        return
    print("-" * 100)
    index = front
    while True:
        print(queue[index], end=' ')
        if index == rear:
            break
        index = (index + 1) % size
    print()
    print("-" * 100)

# Main program
while True:
    print("\nPress 1 for Enqueue (Insert new item at rear end)")
    print("Press 2 for Dequeue (Delete item from front end)")
    print("Press 3 for Display")
    print("Press 0 for Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            value = input("Enter value to insert in circular queue: ")
            enqueue(value)
        case 2:
            dequeue()
        case 3:
            display()
        case 0:
            print("Good bye")
            break
        case _:
            print("Invalid choice")
