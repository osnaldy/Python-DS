class Queue:

    def __init__(self):

        self.items = []

    def is_empty(self):

        return self.items == []

    def enqueue(self, items):

        self.items.insert(0, items)

    def dequeue(self):

        return self.items.pop()

    def size(self):

        return len(self.items)

    def __repr__(self):

        return repr(self.items)
