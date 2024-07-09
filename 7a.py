class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} into the stack.")

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack (top to bottom):", self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} into the queue.")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue (front to rear):", self.items)


print("Testing Stack operations:")

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
print("Peek:", s.peek())
print("Popped:", s.pop())
s.display()
print()
print("Testing Queue operations:")


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Peek:", q.peek())
print("Dequeued:", q.dequeue())
q.display()
print()
print("Testing empty conditions:")


empty_stack = Stack()
print("Empty stack size:", empty_stack.size())

empty_queue = Queue()
print("Empty queue size:", empty_queue.size())
