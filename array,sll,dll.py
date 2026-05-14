comparisons = 0
shifts = 0

array = []
sll = []
dll = []

def reset():
    global comparisons, shifts
    comparisons = 0
    shifts = 0


def create(ds):
    elements = list(map(int, input("Enter elements: ").split()))
    ds.clear()
    ds.extend(elements)


def insert(ds):
    global shifts
    reset()
    pos = int(input("Enter position: "))
    value = int(input("Enter value: "))
    if 0 <= pos <= len(ds):
        ds.insert(pos, value)
        shifts = len(ds) - pos - 1
    else:
        print("Invalid position")


def search(ds):
    global comparisons
    reset()
    value = int(input("Enter value to search: "))
    for i in range(len(ds)):
        comparisons += 1
        if ds[i] == value:
            print("Found at position:", i)
            return
    print("Not found")


def delete(ds):
    global shifts
    reset()
    pos = int(input("Enter position to delete: "))
    if 0 <= pos < len(ds):
        ds.pop(pos)
        shifts = len(ds) - pos
    else:
        print("Invalid position")


def update(ds):
    pos = int(input("Enter position to update: "))
    value = int(input("Enter new value: "))
    if 0 <= pos < len(ds):
        ds[pos] = value
    else:
        print("Invalid position")


def reverse(ds):
    global shifts
    reset()
    left = 0
    right = len(ds) - 1
    while left < right:
        ds[left], ds[right] = ds[right], ds[left]
        shifts += 1
        left += 1
        right -= 1
    print("Reversed successfully")


def display(ds, name):
    print(name, ":", ds)
    print("Comparisons:", comparisons)
    print("Shifts:", shifts)


while True:
    print("\n1.Array\n2.SLL\n3.DLL\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    if choice == 1:
        ds = array
        name = "Array"
    elif choice == 2:
        ds = sll
        name = "Singly Linked List"
    elif choice == 3:
        ds = dll
        name = "Doubly Linked List"
    else:
        continue

    print("1.Create\n2.Insert\n3.Search\n4.Delete\n5.Update\n6.Reverse\n7.Display")
    op = int(input("Enter operation: "))

    if op == 1:
        create(ds)
    elif op == 2:
        insert(ds)
    elif op == 3:
        search(ds)
    elif op == 4:
        delete(ds)
    elif op == 5:
        update(ds)
    elif op == 6:
        reverse(ds)
    elif op == 7:
        display(ds, name)