from MainNode import Node


class OrderedList:

    def __init__(self):

        self.head = None

    def is_empty(self):

        return self.head is None

    def size(self):

        size = self.is_empty()
        if size is None:
            return

        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count

    def remove(self, item):

        current = self.head
        prev = None
        found = False

        while not found:

            if current.get_data() != item:
                return str(item) + " Not found"

            if current.get_data() == item:
                found = True
            else:
                prev = current
                current = current.next

        if prev is None:
            self.head = current.next
        else:
            prev.set_next(current.get_next())

        return current.get_data()

    def search(self, item):

        current = self.head
        stop = False
        found = False

        while current is not None and not found and not stop:

            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.next

        return found

    def sum_elements_of_two_linked_list(self, list1, list2):

        list3 = Node(None)
        carry = 0

        while list1 is not None or list2 is not None:

            if list1 is not None:

                carry += list1.data
                list1 = list1.next

            if list2 is not None:

                carry += list2.data
                list2 = list2.next

            list3.next = Node(carry % 10)
            list3 = list3.next
            carry //= 10

            if self.head is None:
                self.head = list3

            if carry > 0:
                list3.next = Node(carry)
        return list3

    def add(self, item):

        current = self.head
        prev = None
        stop = False

        while current is not None and not stop:

            if current.get_data() > item:
                stop = True

            else:
                prev = current
                current = current.get_next()

        temp = Node(item)

        if prev is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            prev.set_next(temp)

    def print_list(self):

        current = self.head

        while current is not None:

            print (current.get_data(), "-->", end=' ')
            current = current.get_next()
        print(current)

myList = OrderedList()
myList.add(23)
myList.add(77)
myList.add(44)
myList.add(5)

myList2 = OrderedList()
myList2.add(23)
myList2.add(77)
myList2.add(44)
myList2.add(5)

myList3 = OrderedList()
myList3.sum_elements_of_two_linked_list(myList.head, myList2.head)

myList.print_list()
myList2.print_list()
myList3.print_list()