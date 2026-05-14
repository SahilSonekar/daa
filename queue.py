queue = []

def enqueue():

    value = int(input("Enter element to enqueue: "))

    queue.append(value)

    print("Element inserted successfully.")

def dequeue():

    if len(queue) == 0:
        print("Queue is empty")

    else:
        removed = queue.pop(0)

        print("Deleted element:", removed)

def front():

    if len(queue) == 0:
        print("Queue is empty")

    else:
        print("Front element:", queue[0])

def display():

    if len(queue) == 0:
        print("Queue is empty")

    else:
        print("Queue:", queue)

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        front()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")