from MainNode import Node


class UnOrderedList:

    def __init__(self):

        self.head = None

    def is_empty(self):

        return self.head is None

    # ---------------- Function to add a new Node ----------------------
    def add(self, item):
        # Creates a new Node and places the item as its data
        temp = Node(item)
        # Then we need to link the new Node into the existing structure
        # Here we change the next reference of the new Node to refer to the old first Node in the list
        temp.set_next(self.head)
        # Then the head of the list is modify in order to refer to the new Node
        self.head = temp

    # ---------------- Function to return the size of the linked list ----------------------
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

    # ---------------- Function to search for a Node ----------------------
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

    # ---------------- Function to print a Nodes inside the linked list ----------------------
    def print_list(self):

        node = self.head

        while node is not None:
            print(node.data, end=' ')
            node = node.next

    # ---------------- Function to sum two linked list ----------------------

    def sum_two_list(self, head1, head2):

        current = Node(None)
        carry = 0

        while head1 is not None and head2 is not None:

            if head1 is not None:

                carry += head1.data
                head1 = head1.next

            if head2 is not None:

                carry += head2.data
                head2 = head2.next

            current.next = Node(carry % 10)
            current = current.next

            carry //= 10

            if self.head is None:
                self.head = current

            if carry > 0:

                current.next = Node(carry)
        return current.next

    # ---------------- Function to reverse an print linked list ----------------------
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

    # ---------------- Function to insert a new Node at any given index ----------------------
    def insert_after(self, index, item):

        # insert a new Node after a given index
        current = self.head

        for i in range(index):
            current = current.get_next()

        if current is not None:
            new_node = Node(item)
            new_node.set_next(current.get_next())
            current.set_next(new_node)
        else:
            raise("Index is out of range")

    # ---------------- Function to remove a Node ----------------------
    def remove(self, item):

        current = self.head
        prev = None
        found = False

        while not found:

            if current.data != item:
                return "item not found"

            if current.get_data() == item:
                found = True
                # if item is not found, prev and current must move one node ahead
            else:
                prev = current
                current = current.get_next()

        if prev is None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())

        return current.data

    # ---------------- Function to append a Node ----------------------
    def append(self, item):

        # create a new node including item data
        new_node = Node(item)
        # verify if the list is empty, it will assign new node as the head of the list
        if self.head is None:
            return new_node
        # create a pointer to the head
        current = self.head

        # create a loop to verify when the next reference of current become None
        while None is not current.get_next():
            # move forward one position until null is found
            current = current.get_next()
        # assign the new node to the next reference of current which was None
        current.next = new_node

    # ---------------- Function to pop a Node ----------------------

    def pop(self):

        current = self.head
        prev = None

        while current.get_next() is not None:

            prev = current
            current = current.get_next()

        prev.next = None
        return current

    # ---------------- Function to delete first Node ----------------------

    def delete_first(self):

        current = self.head
        self.head = self.head.next
        current.set_next(None)

    # ---------------- Function to return the index of a Node ----------------------

    def return_index(self, item):

        current = self.head
        count = 0

        found = False

        while not found:
            if current.get_data() == item:
                count += 1
                found = True
            else:
                count += 1
                current = current.get_next()
        return count

# ---------------- Function to remove Node at a given position ----------------------

    def pop_pos(self, pos):

        size = self.size()

        if pos > size or pos < 1:
            print("Invalid position given -->", pos)
            return self.head.data

        if pos == 1:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

        else:
            prev = self.head

            for i in range(1, pos - 1):
                prev = prev.get_next()

            current = prev.next
            prev.next = current.next
            current.next = None
            return current.data

myList = UnOrderedList()

myList.add(11)
myList.add(15)
myList.add(8)
myList.add(10)
#myList.add(10)
#myList.insert_after(1, 55)
myList.print_list()
print()
#print(myList.pop_pos(5))
#myList.print_list()
#print(myList.search(8))
# print(myList.search(55)
# myList.append(100)
# myList.print_list()
# print()
# print(myList.return_index(55))
# print()
# print()
print(myList.remove(1))
myList.print_list()
# myList.pop()
# myList.delete_first()
# myList.print_list()
# print(' \nReversed version of Linked List')
# myList.reverse_list()