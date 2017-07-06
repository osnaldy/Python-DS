from MainNode import Node


class UnOrderedList:

    def __init__(self):

        self.head = None

    def is_empty(self):

        return self.head is None

    def add(self, item):
        # Creates a new Node and places the item as its data
        temp = Node(item)
        # Then we need to link the new Node into the existing structure
        # Here we change the next reference of the new Node to refer to the old first Node in the list
        temp.set_next(self.head)
        # Then the head of the list is modify in order to refer to the new Node
        self.head = temp
