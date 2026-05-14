class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = None


def create():

    global head

    n = int(input("Enter number of elements: "))

    for i in range(n):

        value = int(input(f"Enter element {i+1}: "))

        new_node = Node(value)

        if head is None:
            head = new_node

        else:
            temp = head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp


def display():

    temp = head

    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next

    print("None")


def insert():

    global head

    pos = int(input("Enter position to insert (1-based): "))
    value = int(input("Enter value to insert: "))

    new_node = Node(value)

    if pos == 1:

        new_node.next = head

        if head:
            head.prev = new_node

        head = new_node

        print("Element inserted successfully.")
        return

    temp = head

    for i in range(pos - 2):
        temp = temp.next

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next:
        temp.next.prev = new_node

    temp.next = new_node

    print("Element inserted successfully.")


def search():

    value = int(input("Enter element to search: "))

    temp = head
    pos = 1

    while temp:

        if temp.data == value:
            print("Element found at position", pos)
            return

        temp = temp.next
        pos += 1

    print("Element not found")


def delete():

    global head

    pos = int(input("Enter position to delete (1-based): "))

    if pos == 1:

        head = head.next

        if head:
            head.prev = None

        print("Element deleted successfully.")
        return

    temp = head

    for i in range(pos - 1):
        temp = temp.next

    temp.prev.next = temp.next

    if temp.next:
        temp.next.prev = temp.prev

    print("Element deleted successfully.")


def update():

    pos = int(input("Enter position to update (1-based): "))
    value = int(input("Enter new value: "))

    temp = head

    for i in range(pos - 1):
        temp = temp.next

    temp.data = value

    print("Element updated successfully.")


def reverse():

    global head

    temp = head
    prev_node = None

    while temp:

        temp.prev, temp.next = temp.next, temp.prev

        prev_node = temp
        temp = temp.prev

    if prev_node:
        head = prev_node

    print("Doubly Linked List reversed successfully.")


create()

while True:

    print("\n1. Display")
    print("2. Insert")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Reverse")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display()

    elif choice == 2:
        insert()

    elif choice == 3:
        search()

    elif choice == 4:
        delete()

    elif choice == 5:
        update()

    elif choice == 6:
        reverse()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")