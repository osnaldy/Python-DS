from MainNode import Node


class OrderedList:

    def __init__(self):

        self.head = None

    def size(self):

        if self.head is None:
            return

        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count
