class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Front item: {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
        
# Demonstração de funcionamento
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.peek()         # Front item: 1
q.dequeue()      # Dequeued: 1
q.dequeue()      # Dequeued: 2
q.peek()         # Front item: 3
q.dequeue()      # Dequeued: 3
q.dequeue()      # Queue is empty