class Counter:

    def __init__(self):
        self.comparisons = 0
        self.shifts = 0

    def reset(self):
        self.comparisons = 0
        self.shifts = 0


class Stack:

    def __init__(self):
        self.stack = []
        self.counter = Counter()

    def create(self):
        self.stack = []
        self.counter.reset()

    def insert(self, value):
        self.stack.append(value)

    def delete(self):
        if self.stack:
            self.stack.pop()

    def search(self, value):

        for i in range(len(self.stack) - 1, -1, -1):

            self.counter.comparisons += 1

            if self.stack[i] == value:
                return i

        return -1

    def update(self, pos, value):

        if 0 <= pos < len(self.stack):
            self.stack[pos] = value
        else:
            print("Invalid Position")

    def display(self):
        print(self.stack)


class Queue:

    def __init__(self):
        self.queue = []
        self.counter = Counter()

    def create(self):
        self.queue = []
        self.counter.reset()

    def insert(self, value):
        self.queue.append(value)

    def delete(self):

        if self.queue:
            self.queue.pop(0)
            self.counter.shifts += 1

    def search(self, value):

        for i in range(len(self.queue)):

            self.counter.comparisons += 1

            if self.queue[i] == value:
                return i

        return -1

    def update(self, pos, value):

        if 0 <= pos < len(self.queue):
            self.queue[pos] = value
        else:
            print("Invalid Position")

    def display(self):
        print(self.queue)


def show_metrics(ds):

    print("Comparisons:", ds.counter.comparisons)
    print("Shifts:", ds.counter.shifts)


def main():

    stack = Stack()
    queue = Queue()

    while True:

        print("\n===== DATA STRUCTURE MENU =====")
        print("1. Stack")
        print("2. Queue")
        print("0. Exit")

        choice = int(input("Choice: "))

        if choice == 0:
            break

        # STACK
        elif choice == 1:

            while True:

                print("\nSTACK MENU")
                print("1. Create")
                print("2. Push")
                print("3. Pop")
                print("4. Search")
                print("5. Update")
                print("6. Display")
                print("0. Back")

                ch = int(input("Choice: "))

                if ch == 0:
                    break

                elif ch == 1:
                    stack.create()

                elif ch == 2:
                    stack.insert(int(input("Value: ")))

                elif ch == 3:
                    stack.delete()

                elif ch == 4:

                    stack.counter.reset()

                    value = int(input("Value: "))

                    print("Index:", stack.search(value))

                    show_metrics(stack)

                elif ch == 5:

                    pos = int(input("Position: "))
                    value = int(input("Value: "))

                    stack.update(pos, value)

                elif ch == 6:
                    stack.display()

        # QUEUE
        elif choice == 2:

            while True:

                print("\nQUEUE MENU")
                print("1. Create")
                print("2. Enqueue")
                print("3. Dequeue")
                print("4. Search")
                print("5. Update")
                print("6. Display")
                print("0. Back")

                ch = int(input("Choice: "))

                if ch == 0:
                    break

                elif ch == 1:
                    queue.create()

                elif ch == 2:
                    queue.insert(int(input("Value: ")))

                elif ch == 3:

                    queue.counter.reset()

                    queue.delete()

                    show_metrics(queue)

                elif ch == 4:

                    queue.counter.reset()

                    value = int(input("Value: "))

                    print("Index:", queue.search(value))

                    show_metrics(queue)

                elif ch == 5:

                    pos = int(input("Position: "))
                    value = int(input("Value: "))

                    queue.update(pos, value)

                elif ch == 6:
                    queue.display()


main()