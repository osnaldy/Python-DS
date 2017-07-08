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

    def size(self):

        current = self.head
        count = 0

        # Compares the reference to None and increases the count as long as it is not equal to None
        while current is not None:

            count += 1
        # Moves to to next Node item in the list
            current = current.get_next()
        # returns the numbers of Nodes found in the list
        return count

    def search(self, item):

        current = self.head

        # since the item is not found at the start of the Traversal, found is set to false
        found = False

        # Keep looping while there are still items left in the list and and the item has not been found
        while current is not None and not found:

            if current.get_data() == item:

                found = True

            else:

                current = current.get_next()

        return found

    def print_list(self):

        node = self.head

        while node is not None:

            print(node.data, end=' ')

            node = node.next

    def reverse_list(self):

        prev = None
        current = self.head

        while current is not None:

            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        self.head = prev
        self.print_list()

myList = UnOrderedList()

myList.add(17)
myList.add(56)
myList.add(23)
myList.add(60)
myList.add(10)

print(myList.search(60))

myList.print_list()
print(' \nReversed version of Linked List')
myList.reverse_list()




