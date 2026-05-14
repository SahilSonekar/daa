arr = []

def create():
    n = int(input("Enter number of elements: "))

    for i in range(n):
        value = int(input(f"Enter element {i+1}: "))
        arr.append(value)

def display():
    print("Array:", arr)

def insert():
    pos = int(input("Enter position to insert (1-based): "))
    value = int(input("Enter value to insert: "))

    arr.insert(pos - 1, value)
    print("Element inserted successfully.")

def search():
    value = int(input("Enter element to search: "))

    if value in arr:
        print("Element found at position", arr.index(value) + 1)
    else:
        print("Element not found")

def delete():
    pos = int(input("Enter position to delete (1-based): "))

    arr.pop(pos - 1)
    print("Element deleted successfully.")

def update():
    pos = int(input("Enter position to update (1-based): "))
    value = int(input("Enter new value: "))

    arr[pos - 1] = value
    print("Element updated successfully.")

def reverse():
    arr.reverse()
    print("Array reversed successfully.")

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